# SPEED CONVERTER FUNCTION
def speedKMH(kmh):
    """
    Convert speed from km/h to world_units/step.
    
    Args:
        kmh: Speed in kilometers per hour
        
    Returns:
        Speed in world_units/step
        
    Example:
        speedKMH(50)  # Returns 2.1555555555555554 (~= 50 km/h)
    """
    # Conversion factor derived from: 50 km/h = 2.1555555555555554 world_units/step
    # world_units/step = kmh * (2.1555555555555554 / 50)
    return kmh * 0.04311111111111111



# =============================================================================
# DQN TRAINING HYPERPARAMETERS
# =============================================================================
EPSILON_DECAY = 0.998  
TRAIN_MAX_EPSILON = 1.0  
TRAIN_MIN_EPSILON = 0.05  
LEARNING_RATE = 0.001
GAMMA = 0.99
BATCH_SIZE = 512
TARGET_UPDATE_FREQ = 10
MEMORY_SIZE = 50000
DQN_HIDDEN_SIZES = (128, 128, 64)




# =============================================================================
# DEBUG CONFIGURATIONS
# =============================================================================
ValidationTesterMode = False
END_EXACT = True  # Terminates exactly at the CLI --episodes target after saving
INDRUN_FINAL_STAGE = (
    True  # True retains final-stage independent and validation run behavior
)
SAVE_MODEL_CHECKPOINT = 0  # Periodically saves a *_check.pth checkpoint every N episodes




# =============================================================================
# AGENT VEHICLES
# =============================================================================
DECISION_INTERVAL = 10  # A single decision is maintained for 10 simulation steps
TURNING_ANGLE = 5  # Steering target adjustment per left/right decision
CAR_WIDTH = 18
CAR_HEIGHT = 39
USE_PNG = True
CAR_MAX_SPEED = speedKMH(75)  # ~= 292 px/s ~= 75 km/h ~= 20.83 m/s
CAR_MIN_SPEED = speedKMH(55)  # ~= 214 px/s ~= 55 km/h ~= 15.28 m/s
SPEED_UP = 2 # Agent Target Speed by +2 km/h
SPEED_DOWN = -3 # Agent Target Speed by -3 km/h








# =============================================================================
# OBSTACLE VEHICLES
# =============================================================================
OBSTACLE_SPEED = speedKMH(50) # Set all obstacle speed (50 default)
OBSTACLE_WIDTH = 18
OBSTACLE_HEIGHT = 39






# =============================================================================
# SENSOR CONFIGURATION  [R2, R1, F, L1, L2, SR, SL]  (rec: dont change anything)
# =============================================================================
SENSOR_NOISE_RANGE = [0] #[-2,-1,0,1,2]

SENSOR_F = 113.333
SENSOR_L1 = 113.333
SENSOR_R1 = 113.333
SENSOR_L2 = 80
SENSOR_R2 = 80
SENSOR_SL = 40
SENSOR_SR = 40

SENSOR_ANGLE_F = 0
SENSOR_ANGLE_L1 = 15
SENSOR_ANGLE_R1 = -15
SENSOR_ANGLE_L2 = 40
SENSOR_ANGLE_R2 = -40
SENSOR_ANGLE_SL = 110
SENSOR_ANGLE_SR = -110

SENSOR_ANGLES = [
    SENSOR_ANGLE_R2,
    SENSOR_ANGLE_R1,
    SENSOR_ANGLE_F,
    SENSOR_ANGLE_L1,
    SENSOR_ANGLE_L2,
    SENSOR_ANGLE_SR,
    SENSOR_ANGLE_SL,
]








# =============================================================================
# WORLD GEOMETRY AND SIMULATION ENVIRONMENT (rec: dont change anything)
# =============================================================================
LANE_COUNT = 3
LANE_WIDTH = 33  # 33 world units ~= 49.5 px at 1.5 scale
ROAD_WIDTH = LANE_COUNT * LANE_WIDTH
FINISH_DISTANCE = (
    100  # The finish line is consistently placed 100 units beyond the furthest obstacle
)
SCREEN_HEIGHT = 800  # Main viewport height
CAR_STATIC_Y_POS = 150  # Fixed vertical position of the vehicle on screen
DEFAULT_SCALE = 1.5  # 1 world unit = 1.5 pixels
FPS = 60
FONT_TITLE = 24
FONT_SUBTITLE = 20
FONT_TEXT = 18
CONSECUTIVE_SAVE_BEST = 3
CONSECUTIVE_STAGE_REQ = 1
ALLSTAGE_CONSECUTIVE_REQ = 1
INDEPENDENT_BASED = (
    False  # Independent evaluation condition to advance to the next stage
)
SUCCESS_BASED_REQ = 1
INDEPENDENT_COUNT_REQ = 1000000
GRAD_CLIP_MAX_NORM = 1.0
KEYONE_MULTIPLIER = 50
nearmiss_distance = 10
startRandom = 400
gapRandom = 125
maxRandom = 50
START_RANDOM = startRandom
GAP_RANDOM = gapRandom
MAX_RANDOM = maxRandom
TRAIN_MULTIPLIER = 50
visualize_logs_sec = 2
trackMovingDataCsv = 10  # Take data every 10 frames for moving data logs





# =============================================================================
# EXPERIMENTAL MANAGEMENT (rec: dont change anything, this is experimental purposes)
# =============================================================================
ENABLE_EPSILON_RECOVERY = False  
TRAIN_FINAL_MIN_EPSILON = 0.05  # Lower bound epsilon for the final stage when SSC is 0
TRAIN_FINAL_MIN_EPSILON_SSC = 0.05  # Lower bound epsilon for the final stage when SSC > 0
CONSECUTIVE_EPSILON_RECOVERY = 100000000  # Episodes at minimum epsilon before recovery is enforced
CONSECUTIVE_EPSILON_RECOVERY_SSC = 100000000  # Episodes at final-stage SSC minimum epsilon before recovery
AMOUNT_EPSILON_RECOVERY = 0  
NEW_STAGE_EPSILON = 0  
OBSTACLE_ADAPTIVE_SPEED = False
OBSTACLE_MAX_SPEED = OBSTACLE_SPEED
OBSTACLE_MIN_SPEED = OBSTACLE_SPEED
OBSTACLE_STEP_SPEED = 2
OBSTACLE_INTERVAL_SPEED = 60  # 60 fps = every 1 second obstacle random/stay speed
OBSTACLE_SPEED_GRADUAL = 10