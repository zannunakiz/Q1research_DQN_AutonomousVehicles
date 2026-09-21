# =============================================================================
# REWARD SYSTEM
# Reward and penalty configuration used by the environment for shaping DQN
# learning, plus the sensor/offset constants tied to reward behavior.
# =============================================================================
REWARD_PROGRESS = 0  # unused (experimental)
OBSTACLE_WARNING_DISTANCE_FRONT = 60
OBSTACLE_WARNING_DISTANCE_SIDES = 16.4  # Lateral warning sensor distance
TTC_OFFSET = 840  # TTC starts at SENSOR_F (93.333) + 840 world units = 933.333 WORLD UNIT = 100 METER.
TTC_SCALE = 1.5  # 1.5 is default, following applied scale on pygame for realistic value
STRAIGHT_ANGLE_THRESHOLD = 10
LANE_CENTER_REWARD_WIDTH = 8  # Width of the active reward zone near the lane center
SHOW_CENTERLANE_REWARD_INDICATOR = False
CENTERLANE_REWARD_INDICATOR_COLOR = (0, 0, 255, 50)

LEFT_LR_OFFSETX = -3
RIGHT_LR_OFFSETX = 4
CENTER_LR_OFFSETX = 0.5
LEFT_OBSTACLE_OFFSETX = 0.0
RIGHT_OBSTACLE_OFFSETX = 0
CENTER_OBSTACLE_OFFSETX = 0.5


# =============================================================================
# REWARD CONFIGURATION - ADAPTIVE SCHEMA SELECTION
# =============================================================================

# Select the reward schema: "ORIGINAL", "A0", "A1", or "A2"
SELECT_REWARD = "ORIGINAL"  # <-- change this to switch schemas

# -----------------------------------------------------------------------------
# Define all schemas in a dictionary
# -----------------------------------------------------------------------------
REWARD_SCHEMAS = {
    "ORIGINAL": {
        "REWARD_LANE_CENTER_MAX": 0.020,
        "REWARD_STRAIGHT_ANGLE": 0.020,
        "REWARD_FAST_CLEAR": 0.020,
        "REWARD_FINISH": 5.0,
        "PENALTY_COLLISION": -5.0,
        "PENALTY_TIMEOUT": 0.0,
        "PENALTY_WARNING_DISTANCE_FRONT": -0.050,
        "PENALTY_WARNING_DISTANCE_SIDES": -0.030,
        "PENALTY_NOT_IN_CENTER": -0.020,
        "PENALTY_SLOW_WHEN_CLEAR": -0.030,
    },
    "A0": {
        "REWARD_LANE_CENTER_MAX": 0.020,
        "REWARD_STRAIGHT_ANGLE": 0.020,
        "REWARD_FAST_CLEAR": 0.020,
        "REWARD_FINISH": 5.0,
        "PENALTY_COLLISION": -5.0,
        "PENALTY_TIMEOUT": 0.0,
        "PENALTY_WARNING_DISTANCE_FRONT": 0.0,
        "PENALTY_WARNING_DISTANCE_SIDES": 0.0,
        "PENALTY_NOT_IN_CENTER": -0.020,
        "PENALTY_SLOW_WHEN_CLEAR": -0.030,
    },
    "A1": {
        "REWARD_LANE_CENTER_MAX": 0.020,
        "REWARD_STRAIGHT_ANGLE": 0.020,
        "REWARD_FAST_CLEAR": 0.020,
        "REWARD_FINISH": 5.0,
        "PENALTY_COLLISION": -5.0,
        "PENALTY_TIMEOUT": 0.0,
        "PENALTY_WARNING_DISTANCE_FRONT": -0.050,
        "PENALTY_WARNING_DISTANCE_SIDES": -0.030,
        "PENALTY_NOT_IN_CENTER": -0.020,
        "PENALTY_SLOW_WHEN_CLEAR": -0.030,
    },
    "A2": {
        "REWARD_LANE_CENTER_MAX": 0.020,
        "REWARD_STRAIGHT_ANGLE": 0.020,
        "REWARD_FAST_CLEAR": 0.020,
        "REWARD_FINISH": 5.0,
        "PENALTY_COLLISION": -10.0,
        "PENALTY_TIMEOUT": 0.0,
        "PENALTY_WARNING_DISTANCE_FRONT": -0.100,
        "PENALTY_WARNING_DISTANCE_SIDES": -0.060,
        "PENALTY_NOT_IN_CENTER": -0.020,
        "PENALTY_SLOW_WHEN_CLEAR": -0.030,
    },
}

# -----------------------------------------------------------------------------
# Apply the selected schema to global variables (all importable)
# -----------------------------------------------------------------------------
_selected = REWARD_SCHEMAS[SELECT_REWARD]
REWARD_LANE_CENTER_MAX = _selected["REWARD_LANE_CENTER_MAX"]
REWARD_STRAIGHT_ANGLE = _selected["REWARD_STRAIGHT_ANGLE"]
REWARD_FAST_CLEAR = _selected["REWARD_FAST_CLEAR"]
REWARD_FINISH = _selected["REWARD_FINISH"]
PENALTY_COLLISION = _selected["PENALTY_COLLISION"]
PENALTY_TIMEOUT = _selected["PENALTY_TIMEOUT"]
PENALTY_WARNING_DISTANCE_FRONT = _selected["PENALTY_WARNING_DISTANCE_FRONT"]
PENALTY_WARNING_DISTANCE_SIDES = _selected["PENALTY_WARNING_DISTANCE_SIDES"]
PENALTY_NOT_IN_CENTER = _selected["PENALTY_NOT_IN_CENTER"]
PENALTY_SLOW_WHEN_CLEAR = _selected["PENALTY_SLOW_WHEN_CLEAR"]

# Clean up temporary variable
del _selected
