# =============================================================================
# RULE-BASED REWARD SYSTEM
# Used when running with --rulebased flag (run_train.py / run_loadmodel.py).
# Replaces the DQN reward schema from config_reward.py with a simple
# engineering rule-based baseline for research comparison purposes.
#
# Sensor layout:  [R2, R1, F, L1, L2, SR, SL]  (indices 0..6)
#   - R2  (idx 0): far-right diagonal forward sensor
#   - R1  (idx 1): near-right diagonal forward sensor
#   - F   (idx 2): front sensor
#   - L1  (idx 3): near-left diagonal forward sensor
#   - L2  (idx 4): far-left diagonal forward sensor
#   - SR  (idx 5): side-right sensor (perpendicular)
#   - SL  (idx 6): side-left sensor (perpendicular)
#
# Action space:
#   0=slow_left, 1=slow_straight, 2=slow_right
#   3=fast_left, 4=fast_straight, 5=fast_right
# =============================================================================

# Rewards
REWARD_MOVETO_CLEARSIDE = 0.020   # Moving toward the safer side (more free space)
REWARD_SLOW_WHEN_DETECT = 0.020   # Front sensor detects obstacle + slow action used
REWARD_FAST_WHEN_CLEAR  = 0.020   # Front sensor is clear + fast straight action used
REWARD_FINISH           = 5.0     # Reached the finish line

# Penalties
PENALTY_MOVETO_UNCLEARSIDE = -0.020  # Moving toward the less safe (more blocked) side
PENALTY_COLLISION          = -5.0   # Collision with obstacle or road boundary

# Threshold (normalized sensor value 0..1) above which the front is "clear".
# Normalized sensor value = distance / max_range; 1.0 = nothing detected.
# 0.80 means the front obstacle is farther than 80% of the sensor range.

# Example if threshold value 0.80:
# = 0.90 → assuming clear
# = 0.75 → assuming obstacle detected
RULEBASED_FRONT_CLEAR_THRESHOLD = 0.80
# * Want to detect obstacles even if they are very small or far away: **increase the threshold**, for example, `0.90` or `0.95`.
# * Want to wait until the obstacle is really close: **decrease the threshold**, for example, `0.50` or `0.30`.

