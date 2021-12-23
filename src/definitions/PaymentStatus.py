from enum import Enum, auto


class PaymentStatus(Enum):
    Unpaid = auto()
    Deferred = auto()
    Paid = auto()
