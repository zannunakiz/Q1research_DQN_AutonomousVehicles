# =============================================================================
# MAIN LOGGER
# Consolidated logging / data utilities: TTC (time-to-collision) helpers and
# moving-data CSV tracking.
# =============================================================================
import csv
import json
import math
import os
from math import isfinite

from func_scale import to_kmh, to_meter
from config_reward import OBSTACLE_WARNING_DISTANCE_FRONT, TTC_OFFSET, TTC_SCALE


# =============================================================================
# TTC (TIME-TO-COLLISION)
# =============================================================================
TTC_SENSOR_INDICES = (0, 1, 2, 3, 4)
TTC_FRONT_SENSOR_INDEX = 2


def _safe_float(value, default=0.0):
    try:
        result = float(value)
    except (TypeError, ValueError):
        return float(default)
    if not isfinite(result):
        return float(default)
    return result


def _lane_from_x(x_value, lane_width, lane_count):
    lane_width = max(_safe_float(lane_width, 1.0), 1e-9)
    lane_count = max(int(lane_count), 1)
    lane = int(_safe_float(x_value, 0.0) // lane_width)
    return max(0, min(lane_count - 1, lane))


def format_ttc_ms(ttc_ms):
    if ttc_ms is None:
        return "None"
    return f"{float(ttc_ms):.3f}"


def summarize_ttc_samples(ttc_samples):
    values = [float(value) for value in ttc_samples if value is not None]
    if not values:
        return {"min_ttc": None, "avg_ttc": None, "count": 0}
    return {
        "min_ttc": min(values),
        "avg_ttc": sum(values) / len(values),
        "count": len(values),
    }


def _scale_ttc_ms(ttc_ms):
    if ttc_ms is None:
        return None
    return float(ttc_ms) * _safe_float(TTC_SCALE, 1.0)


def calculate_ttc_ms(
    car_x,
    car_y,
    car_height,
    car_speed,
    obstacles,
    lane_width,
    lane_count,
    sensor_ranges,
):
    details = calculate_ttc_details(
        car_x=car_x,
        car_y=car_y,
        car_height=car_height,
        car_speed=car_speed,
        obstacles=obstacles,
        lane_width=lane_width,
        lane_count=lane_count,
        sensor_ranges=sensor_ranges,
    )
    return details["ttc_ms"]


def calculate_ttc_details(
    car_x,
    car_y,
    car_height,
    car_speed,
    obstacles,
    lane_width,
    lane_count,
    sensor_ranges,
):
    """
    Return current TTC details for front-sensor vehicle targets.

    TTC is only valid when an obstacle vehicle is in the same lane, ahead of the
    agent, inside the configured F sensor range plus TTC_OFFSET, and the agent is
    closing the distance. Road boundaries and side sensors are excluded.
    """
    ranges = list(sensor_ranges or [])
    front_ranges = ranges[: len(TTC_SENSOR_INDICES)]
    if not front_ranges:
        return {"ttc_ms": None, "target_index": None, "counting": False}
    front_sensor_range = _safe_float(
        ranges[TTC_FRONT_SENSOR_INDEX] if len(ranges) > TTC_FRONT_SENSOR_INDEX else 0.0
    )
    configured_ttc_range = front_sensor_range + _safe_float(TTC_OFFSET)
    ttc_range = max(0.0, configured_ttc_range)
    if ttc_range <= 0:
        return {"ttc_ms": None, "target_index": None, "counting": False}

    agent_lane = _lane_from_x(car_x, lane_width, lane_count)
    car_y_value = _safe_float(car_y)
    car_half_height = _safe_float(car_height) / 2.0
    car_bottom = car_y_value - car_half_height
    car_top = car_y_value + car_half_height
    car_speed_kmh = to_kmh(_safe_float(car_speed))

    best_ttc_ms = None
    best_index = None
    for obstacle_index, obstacle in enumerate(obstacles or []):
        if not isinstance(obstacle, dict):
            continue

        obs_lane = _lane_from_x(obstacle.get("x", 0.0), lane_width, lane_count)
        if obs_lane != agent_lane:
            continue

        obs_height = _safe_float(obstacle.get("height", 0.0))
        obs_y = _safe_float(obstacle.get("y", 0.0))
        obs_bottom = obs_y - (obs_height / 2.0)
        obs_top = obs_y + (obs_height / 2.0)
        if obs_top < car_bottom:
            continue
        gap_world = obs_bottom - car_top
        if gap_world < 0:
            gap_world = 0.0
        if gap_world > ttc_range:
            continue

        obs_speed_kmh = to_kmh(_safe_float(obstacle.get("speed", 0.0)))
        relative_speed_kmh = car_speed_kmh - obs_speed_kmh
        if relative_speed_kmh <= 1e-9:
            continue

        distance_m = to_meter(gap_world)
        relative_speed_mps = relative_speed_kmh / 3.6
        ttc_ms = _scale_ttc_ms((distance_m / relative_speed_mps) * 1000.0)
        if best_ttc_ms is None or ttc_ms < best_ttc_ms:
            best_ttc_ms = ttc_ms
            best_index = obstacle_index

    return {
        "ttc_ms": best_ttc_ms,
        "target_index": best_index,
        "counting": best_ttc_ms is not None,
    }


def calculate_env_ttc_ms(env):
    return calculate_env_ttc_details(env)["ttc_ms"]
# =============================================================================
# MOVING DATA CSV (logging)
# =============================================================================
MOVING_DATA_CSV_NAME = "movingData.csv"
MOVING_DATA_CSV_HEADERS = [
    "episode",
    "mov_avgttc",
    "mov_speed",
    "mov_angle",
    "mov_posx",
]


def format_avg_speed(speed_samples) -> str:
    values = [float(value) for value in speed_samples if _is_finite(value)]
    if not values:
        return "0.0"
    return f"{(sum(values) / len(values)):.1f}"


def format_avg_inference_time(inference_time_ms_samples) -> str:
    values = [
        float(value) for value in inference_time_ms_samples if _is_finite(value)
    ]
    if not values:
        return "0.0000"
    return f"{(sum(values) / len(values)):.4f}"


def new_moving_data_track() -> dict:
    return {
        "mov_avgttc": [],
        "mov_speed": [],
        "mov_angle": [],
        "mov_posx": [],
    }


def should_track_moving_frame(frame_number, interval) -> bool:
    try:
        frame = int(frame_number)
        interval = int(interval)
    except (TypeError, ValueError):
        return False
    return interval > 0 and frame > 0 and frame % interval == 0


def append_moving_data_sample(track: dict, env, ttc_samples) -> None:
    if track is None:
        return

    ttc_summary = summarize_ttc_samples(ttc_samples)
    track.setdefault("mov_avgttc", []).append(
        _rounded_or_none(ttc_summary.get("avg_ttc"), 2)
    )
    track.setdefault("mov_speed", []).append(
        _rounded_or_none(to_kmh(getattr(env, "car_speed", 0.0)), 1)
    )
    track.setdefault("mov_angle", []).append(
        _rounded_or_none(_vehicle_relative_angle(env), 1)
    )
    track.setdefault("mov_posx", []).append(
        _rounded_or_none(getattr(env, "car_x", 0.0), 1)
    )


def build_moving_data_row(episode: int, track: dict) -> dict:
    track = track or new_moving_data_track()
    return {
        "episode": int(episode),
        "mov_avgttc": _json_array(track.get("mov_avgttc", []), 2),
        "mov_speed": _json_array(track.get("mov_speed", []), 1),
        "mov_angle": _json_array(track.get("mov_angle", []), 1),
        "mov_posx": _json_array(track.get("mov_posx", []), 1),
    }


def get_moving_data_csv_path(base_csv_path=None, base_dir=None, csv_name=None):
    if base_csv_path:
        directory = os.path.dirname(os.path.abspath(base_csv_path))
    elif base_dir:
        directory = os.path.abspath(base_dir)
    else:
        directory = os.getcwd()
    filename = csv_name if csv_name else MOVING_DATA_CSV_NAME
    return os.path.join(directory, filename)


def save_moving_data_csv(csv_path: str, rows, current_row=None) -> None:
    directory = os.path.dirname(os.path.abspath(csv_path))
    os.makedirs(directory, exist_ok=True)
    with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=MOVING_DATA_CSV_HEADERS)
        writer.writeheader()
        for row in rows or []:
            writer.writerow(row)
        if current_row is not None:
            writer.writerow(current_row)


def _is_finite(value) -> bool:
    try:
        return math.isfinite(float(value))
    except (TypeError, ValueError):
        return False


def _rounded_or_none(value, decimals: int):
    if not _is_finite(value):
        return None
    rounded = round(float(value), int(decimals))
    if rounded == -0.0:
        rounded = 0.0
    return rounded


def _json_array(values, decimals: int) -> str:
    rounded_values = [_rounded_or_none(value, decimals) for value in values]
    return json.dumps(rounded_values, separators=(",", ":"))


def _vehicle_relative_angle(env) -> float:
    if hasattr(env, "steering_offset"):
        return float(getattr(env, "steering_offset", 0.0))
    car_angle = float(getattr(env, "car_angle", 0.0))
    base_angle = float(getattr(env, "base_car_angle", 90.0))
    return car_angle - base_angle


def calculate_env_ttc_details(env):
    return calculate_ttc_details(
        car_x=getattr(env, "car_x", 0.0),
        car_y=getattr(env, "car_y", 0.0),
        car_height=getattr(env, "car_height", 0.0),
        car_speed=getattr(env, "car_speed", 0.0),
        obstacles=getattr(env, "obstacles", []),
        lane_width=getattr(env, "lane_width", 1.0),
        lane_count=getattr(env, "lane_count", 1),
        sensor_ranges=getattr(env, "sensor_ranges", []),
    )