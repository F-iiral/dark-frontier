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

class PlanetDefenses(enum.Enum):
    AA_GUN          = 1
    ROCKET          = 2
    RAILGUN         = 3
    LASER           = 4
    ION             = 5
    PLASMA          = 6
    DISRUPTOR       = 7
    SHIELD_S        = 8
    SHIELD_M        = 9
    SHIELD_L        = 10

class FleetShips(enum.Enum):
    FIGHTERS           = 0
    INTERCEPTORS       = 1
    TAC_BOMBERS        = 2
    STR_BOMBERS        = 3
    FRIGATES           = 4
    DESTROYERS         = 5
    CRUISERS           = 6
    BATTLECRUISERS     = 7
    BATTLESHIPS        = 8
    ESCORT_CARRIERS    = 9
    FLEET_CARRIERS     = 10
    TITANS             = 11
    SATTELITES         = 12
    SMALL_CARGO_SHIPS  = 13
    BIG_CARGO_SHIPS    = 14
    COLONY_SHIPS       = 15
    SCIENCE_SHIPS      = 16
    CONSTRUCTION_SHIPS = 17