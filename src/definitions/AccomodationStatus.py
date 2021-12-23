from enum import Enum, auto


class AccomodationStatus(Enum):
    Reserved = auto()
    Canceled = auto()
    Accommodated = auto()
    Ended = auto()
