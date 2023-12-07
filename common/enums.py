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