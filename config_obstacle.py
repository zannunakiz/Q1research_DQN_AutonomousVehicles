from func_scale import meter_to_pygame


def UseSeed(seed_name: str) -> str:
    """Return a seed name for deferred resolution after configuration loading."""
    return seed_name


# =============================================================================
# OBSTACLE CONFIGURATION
# Central place to define and switch between obstacle scenario sets.
#
# To change which obstacle set is used, edit the OBSTACLES assignment below
# and point it to one of the predefined seed configurations:
#
#   MT_SEED   = Main Training and Evaluation Obstacles
#   HP_SEED   = Hyperparameters Tuning Obstacles
#   TM_SEED_1 = Training Method Comparison Obstacles 1
#   TM_SEED_2 = Training Method Comparison Obstacles 2
#   TM_SEED_3 = Training Method Comparison Obstacles 3
#   AB_SEED   = Ablation Study Obstacles (A0-A2)
#   OOD_SEED  = Unseen Robustness Obstacles
#   R_SEED_1  = Robustness Seed 1 (speed and density)
#   R_SEED_2  = Robustness Seed 2 (speed)
#   R_SEED_3  = Robustness Seed 3 (density)
# =============================================================================
# Select the obstacle seed used by training and evaluation.

OBSTACLES = UseSeed("MT_SEED") # Default: MT_SEED for main training


# =============================================================================
# SCENARIO 1: MAIN TRAINING
# The primary training progression used for the standard full training run.
# =============================================================================
MT_SEED = [
    [
        {"lane": 1, "y": 200},
        {"lane": 0, "y": 385},
        {"lane": 2, "y": 385},  #
    ],
    [
        {"lane": 1, "y": 200},
        {"lane": 0, "y": 385},
        {"lane": 2, "y": 385},  #
        {"lane": 1, "y": 570},
        {"lane": 2, "y": 570},
        {"lane": 0, "y": 755},
        {"lane": 2, "y": 755},  #
    ],
    [
        {"lane": 1, "y": 200},
        {"lane": 0, "y": 385},
        {"lane": 2, "y": 385},  #
        {"lane": 1, "y": 570},
        {"lane": 2, "y": 570},
        {"lane": 0, "y": 755},
        {"lane": 2, "y": 755},  #
        {"lane": 1, "y": 940},
        {"lane": 0, "y": 940},
        {"lane": 1, "y": 1125},
        {"lane": 2, "y": 1125},
        {"lane": 1, "y": 1310},
        {"lane": 0, "y": 1310},  #
    ],
]


# =============================================================================
# SCENARIO 2: HYPERPARAMETERS TUNING
# A denser obstacle progression used while sweeping DQN hyperparameters.
# =============================================================================
HP_SEED = [
    [
        {"lane": 1, "y": 200},
        {"lane": 0, "y": 385},
        {"lane": 2, "y": 385},
        {"lane": 1, "y": 570},
        {"lane": 2, "y": 570},
        {"lane": 0, "y": 755},
        {"lane": 2, "y": 755},
    ],
]


# =============================================================================
# SCENARIO 3-5: TRAINING METHOD COMPARISON
# Obstacle sets used to compare curriculum and direct training methods fairly.
# =============================================================================
TM_SEED_1 = [
    [
        {"lane": 1, "y": 200},
    ],
    [
        {"lane": 1, "y": 200},
        {"lane": 0, "y": 385},
        {"lane": 2, "y": 385},
    ],
    [
        {"lane": 1, "y": 200},
        {"lane": 0, "y": 385},
        {"lane": 2, "y": 385},
        {"lane": 1, "y": 570},
        {"lane": 2, "y": 570},
    ],
]

TM_SEED_2 = [
    [
        {"lane": 0, "y": 200},
        {"lane": 1, "y": 200},
    ],
    [
        {"lane": 0, "y": 200},
        {"lane": 1, "y": 200},
        {"lane": 2, "y": 385},
        {"lane": 1, "y": 385},
    ],
    [
        {"lane": 0, "y": 200},
        {"lane": 1, "y": 200},
        {"lane": 2, "y": 385},
        {"lane": 1, "y": 385},
        {"lane": 0, "y": 570},
        {"lane": 1, "y": 570},
    ],
]

TM_SEED_3 = [
    [
        {"lane": 0, "y": 200},
        {"lane": 2, "y": 200},
    ],
    [
        {"lane": 0, "y": 200},
        {"lane": 2, "y": 200},
        {"lane": 1, "y": 385},
        {"lane": 0, "y": 570},
        {"lane": 2, "y": 570},
    ],
    [
        {"lane": 0, "y": 200},
        {"lane": 2, "y": 200},
        {"lane": 1, "y": 385},
        {"lane": 0, "y": 570},
        {"lane": 2, "y": 570},
        {"lane": 0, "y": 755},
        {"lane": 1, "y": 755},
    ],
]


# =============================================================================
# SCENARIO 6: ABLATION
# Obstacles used to test reward schema ablation A0-A2
# =============================================================================
AB_SEED = [
    [
        {"lane": 1, "y": 200},
        {"lane": 2, "y": 200},
        {"lane": 0, "y": 385},
    ],
        [
        {"lane": 1, "y": 200},
        {"lane": 2, "y": 200},
        {"lane": 0, "y": 385},
        {"lane": 1, "y": 435},
        {"lane": 2, "y": 620},
    ],
        [
        {"lane": 1, "y": 200},
        {"lane": 2, "y": 200},
        {"lane": 0, "y": 385},
        {"lane": 1, "y": 435},
        {"lane": 2, "y": 620},
        {"lane": 0, "y": 805},
        {"lane": 2, "y": 805},
        {"lane": 1, "y": 990},
    ],
]


# =============================================================================
# SCENARIO 7: UNSEEN ROBUSTNESS
# Obstacles used to test robustness against patterns not seen in training.
# =============================================================================
OOD_SEED = [
    [
        {"lane": 1, "y": 200},
        {"lane": 2, "y": 385},
        {"lane": 0, "y": 385},
    ],
]


OBSTACLE_GAP = meter_to_pygame(
    20
)  # Default meter_to_pygame(20) equivalent to 20 meters


# Controlled Gap
def CG(x: float) -> float:
    return 200 + (x * OBSTACLE_GAP)


R_SEED_1 = [
    [
        {"lane": 1, "y": 200},
        {"lane": 2, "y": CG(1)},
        {"lane": 0, "y": CG(1)},
        {"lane": 0, "y": CG(2)},
        {"lane": 1, "y": CG(2)},
        {"lane": 2, "y": CG(3)},
        {"lane": 1, "y": CG(3)},
        {"lane": 0, "y": CG(4)},
        {"lane": 1, "y": CG(4)},
        {"lane": 2, "y": CG(5)},
        {"lane": 1, "y": CG(5)},
    ],
]
R_SEED_2 = [
    [
        {"lane": 0, "y": 200},
        {"lane": 1, "y": 200},
        {"lane": 0, "y": 250},
        {"lane": 1, "y": 250},
        {"lane": 0, "y": 300},
        {"lane": 1, "y": 300},
        {"lane": 2, "y": 485},
        {"lane": 1, "y": 485},
        {"lane": 2, "y": 535},
        {"lane": 1, "y": 535},
        {"lane": 2, "y": 585},
        {"lane": 1, "y": 585},
        {"lane": 0, "y": 770},
        {"lane": 2, "y": 770},
        {"lane": 0, "y": 820},
        {"lane": 2, "y": 820},
        {"lane": 0, "y": 870},
        {"lane": 2, "y": 870},
        {"lane": 1, "y": 1055},
    ],
]

R_SEED_3 = [
    [
        {"lane": 0, "y": CG(0)},
        {"lane": 1, "y": CG(1)},
        {"lane": 2, "y": CG(2)},
        {"lane": 1, "y": CG(3)},
        {"lane": 0, "y": CG(4)},
        {"lane": 1, "y": CG(5)},
        {"lane": 2, "y": CG(6)},
        {"lane": 1, "y": CG(7)},
        {"lane": 0, "y": CG(8)},
    ]
]


# =============================================================================
# RESOLVER
# Returns the selected obstacle list. Falls back to MT_SEED for invalid input
# so the simulation always has a valid configuration.
# =============================================================================
def get_obstacles(obstacles=None) -> list:
    """Return the configured obstacle list or an optional list override.

    Args:
        obstacles: Optional obstacle configuration override. If omitted, uses
            the module-level ``OBSTACLES`` value.

    Returns:
        The list-of-stages obstacle configuration for the selected scenario.
    """
    selected = OBSTACLES if obstacles is None else obstacles
    if isinstance(selected, str):
        selected = globals().get(selected)
    return selected if isinstance(selected, list) else MT_SEED


# Concrete alias of the resolved set, for observers that want the list directly.
TRAINING_OBSTACLES = get_obstacles()

# =============================================================================
# TESTER STAGES
# TEST_OBSTACLES are utilized for model validation post-training.
# The trailing numerical comments serve as stage tester references.
# =============================================================================
TO_Y1 = 200
TO_Y2 = 385  # 20 meters gap
TEST_OBSTACLES = [
    # Single obstacles and early obstacle pairs.
    [{"lane": 0, "y": TO_Y1}],  # 1
    [{"lane": 1, "y": TO_Y1}],  # 2
    [{"lane": 2, "y": TO_Y1}],  # 3
    [{"lane": 0, "y": TO_Y1}, {"lane": 2, "y": TO_Y1}],  # 4
    [{"lane": 1, "y": TO_Y1}, {"lane": 0, "y": TO_Y1}],  # 5
    [{"lane": 1, "y": TO_Y1}, {"lane": 2, "y": TO_Y1}],  # 6
    # Base obstacles initiating from the left lane.
    [{"lane": 0, "y": TO_Y1}, {"lane": 0, "y": TO_Y2}],  # 7
    [{"lane": 0, "y": TO_Y1}, {"lane": 1, "y": TO_Y2}],  # 8
    [{"lane": 0, "y": TO_Y1}, {"lane": 2, "y": TO_Y2}],  # 9
    [{"lane": 0, "y": TO_Y1}, {"lane": 0, "y": TO_Y2}, {"lane": 2, "y": TO_Y2}],  # 10
    [{"lane": 0, "y": TO_Y1}, {"lane": 1, "y": TO_Y2}, {"lane": 0, "y": TO_Y2}],  # 11
    [{"lane": 0, "y": TO_Y1}, {"lane": 1, "y": TO_Y2}, {"lane": 2, "y": TO_Y2}],  # 12
    # Base obstacles initiating from the center lane.
    [{"lane": 1, "y": TO_Y1}, {"lane": 0, "y": TO_Y2}],  # 13
    [{"lane": 1, "y": TO_Y1}, {"lane": 1, "y": TO_Y2}],  # 14
    [{"lane": 1, "y": TO_Y1}, {"lane": 2, "y": TO_Y2}],  # 15
    [{"lane": 1, "y": TO_Y1}, {"lane": 0, "y": TO_Y2}, {"lane": 2, "y": TO_Y2}],  # 16
    [{"lane": 1, "y": TO_Y1}, {"lane": 1, "y": TO_Y2}, {"lane": 0, "y": TO_Y2}],  # 17
    [{"lane": 1, "y": TO_Y1}, {"lane": 1, "y": TO_Y2}, {"lane": 2, "y": TO_Y2}],  # 18
    # Base obstacles initiating from the right lane.
    [{"lane": 2, "y": TO_Y1}, {"lane": 0, "y": TO_Y2}],  # 19
    [{"lane": 2, "y": TO_Y1}, {"lane": 1, "y": TO_Y2}],  # 20
    [{"lane": 2, "y": TO_Y1}, {"lane": 2, "y": TO_Y2}],  # 21
    [{"lane": 2, "y": TO_Y1}, {"lane": 0, "y": TO_Y2}, {"lane": 2, "y": TO_Y2}],  # 22
    [{"lane": 2, "y": TO_Y1}, {"lane": 1, "y": TO_Y2}, {"lane": 0, "y": TO_Y2}],  # 23
    [{"lane": 2, "y": TO_Y1}, {"lane": 1, "y": TO_Y2}, {"lane": 2, "y": TO_Y2}],  # 24
    # Base obstacles initiating with dual parallel placements.
    [{"lane": 0, "y": TO_Y1}, {"lane": 2, "y": TO_Y1}, {"lane": 0, "y": TO_Y2}],  # 25
    [{"lane": 0, "y": TO_Y1}, {"lane": 2, "y": TO_Y1}, {"lane": 1, "y": TO_Y2}],  # 26
    [{"lane": 0, "y": TO_Y1}, {"lane": 2, "y": TO_Y1}, {"lane": 2, "y": TO_Y2}],  # 27
    [
        {"lane": 0, "y": TO_Y1},
        {"lane": 2, "y": TO_Y1},
        {"lane": 0, "y": TO_Y2},
        {"lane": 2, "y": TO_Y2},
    ],  # 28
    [
        {"lane": 0, "y": TO_Y1},
        {"lane": 2, "y": TO_Y1},
        {"lane": 1, "y": TO_Y2},
        {"lane": 0, "y": TO_Y2},
    ],  # 29
    [
        {"lane": 0, "y": TO_Y1},
        {"lane": 2, "y": TO_Y1},
        {"lane": 1, "y": TO_Y2},
        {"lane": 2, "y": TO_Y2},
    ],  # 30
    # Base obstacles exploring center-left combinations.
    [{"lane": 1, "y": TO_Y1}, {"lane": 0, "y": TO_Y1}, {"lane": 0, "y": TO_Y2}],  # 31
    [{"lane": 1, "y": TO_Y1}, {"lane": 0, "y": TO_Y1}, {"lane": 1, "y": TO_Y2}],  # 32
    [{"lane": 1, "y": TO_Y1}, {"lane": 0, "y": TO_Y1}, {"lane": 2, "y": TO_Y2}],  # 33
    [
        {"lane": 1, "y": TO_Y1},
        {"lane": 0, "y": TO_Y1},
        {"lane": 0, "y": TO_Y2},
        {"lane": 2, "y": TO_Y2},
    ],  # 34
    [
        {"lane": 1, "y": TO_Y1},
        {"lane": 0, "y": TO_Y1},
        {"lane": 1, "y": TO_Y2},
        {"lane": 0, "y": TO_Y2},
    ],  # 35
    [
        {"lane": 1, "y": TO_Y1},
        {"lane": 0, "y": TO_Y1},
        {"lane": 1, "y": TO_Y2},
        {"lane": 2, "y": TO_Y2},
    ],  # 36
    # Base obstacles exploring center-right combinations.
    [{"lane": 1, "y": TO_Y1}, {"lane": 2, "y": TO_Y1}, {"lane": 0, "y": TO_Y2}],  # 37
    [{"lane": 1, "y": TO_Y1}, {"lane": 2, "y": TO_Y1}, {"lane": 1, "y": TO_Y2}],  # 38
    [{"lane": 1, "y": TO_Y1}, {"lane": 2, "y": TO_Y1}, {"lane": 2, "y": TO_Y2}],  # 39
    [
        {"lane": 1, "y": TO_Y1},
        {"lane": 2, "y": TO_Y1},
        {"lane": 0, "y": TO_Y2},
        {"lane": 2, "y": TO_Y2},
    ],  # 40
    [
        {"lane": 1, "y": TO_Y1},
        {"lane": 2, "y": TO_Y1},
        {"lane": 1, "y": TO_Y2},
        {"lane": 0, "y": TO_Y2},
    ],  # 41
    [
        {"lane": 1, "y": TO_Y1},
        {"lane": 2, "y": TO_Y1},
        {"lane": 1, "y": TO_Y2},
        {"lane": 2, "y": TO_Y2},
    ],  # 42
]
