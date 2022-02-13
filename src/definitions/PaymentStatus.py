from enum import Enum


class PaymentStatus(Enum):

    Unpaid = (
        'unpaid',
        'Rezerwacja nieopłacona'
    )

    Deferred = (
        'deferred',
        'Płatność odroczona'
    )

    Paid = (
        'paid',
        'Rezerwacja opłacona'
    )

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _, description):
        self.description = description
