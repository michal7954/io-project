from enum import Enum, auto


class AccomodationStatus(Enum):
    
    Reserved = (
        'reserved',
        'zarezerwowana'
    )

    Canceled = (
        'canceled',
        'anulowana'
    )

    Accommodated = (
        'accommodated',
        'zakwaterowanie'
    )

    Ended = (
        'ended',
        'zakończona'
    )
    

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _, description):
        self.description = description