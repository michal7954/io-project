from enum import Enum


class Params(Enum):
    # przykładowy parametr = (
    #     identyfikator parametru: "przykładowy parametr",
    #     opis parametru
    # )
    roomNumber = (
        "roomNumber",
        "Podaj numer pokoju",
    )
    roomSize = (
        "roomSize",
        "Podaj rozmiar pokoju",
    )
    roomID = (
        "roomID",
        "Podaj #ID pokoju"
    )

    reservationStart = (
        "reservationStart",
        "Podaj datę początku rezerwacji [DD.MM.RRRR]"
    )
    reservationEnd = (
        "reservationEnd",
        "Podaj datę końca rezerwacji [DD.MM.RRRR]"
    )

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _, description):
        self.description = description

    def text(self):
        return self.description + ": "
