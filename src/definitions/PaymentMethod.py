from enum import Enum, auto


class PaymentMethod(Enum):

    NotChosen = (
        'notChosen',
        ''
    )

    Cash = (
        'cash',
        'gotówka'
    )

    Card = (
        'card',
        'karta'
    )

    Phone = (
        'phone',
        'telefon'
    )

    Blik = (
        'blik',
        'BLIK'
    )

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _, description):
        self.description = description

    def match(self, input):
        return self.description != '' and self.description == input
