from enum import Enum, auto


class ServiceStatus(Enum):

    Pending = (
        'pending',
        'w trakcie realizacji'
    )

    Done = (
        'done',
        'zrealizowana'
    )
    

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _, description):
        self.description = description