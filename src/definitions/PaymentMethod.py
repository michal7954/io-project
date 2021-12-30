from enum import Enum, auto


class PaymentMethod(Enum):
    NotChosen = auto()
    Cash = auto()
    Card = auto()
    Phone = auto()
    Blik = auto()
