import enum

class Badges(enum.Enum):
    ADMINISTRATOR = 1
    MODERATOR = 2
    BANNED = 4
    INACTIVE_SHORT = 8
    INACTIVE_LONG = 16
    VACATION = 32

class Activity(enum.Enum):
    OFFLINE = 0
    ACTIVE = 1
    IDLE = 2
    DND = 3

class PlanetBuildings(enum.Enum):
    METAL_MINE      = 1
    CRYSTAL_MINE    = 2
    GAS_MINE        = 3
    METAL_STORAGE   = 4
    CRYSTAL_STORAGE = 5
    GAS_STORAGE     = 6
    FACTORY         = 7
    SHIPYARD        = 8
    LABORATORY      = 9
    TERRAFORMER     = 10