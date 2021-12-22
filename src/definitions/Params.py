from enum import Enum


class Params(Enum):
    # definicje wszystkich możliwych parametrów podawanych przez użytkownika w aplikacji

    # przykładowy parametr = (
    #     identyfikator parametru: "przykładowy parametr",
    #     opis parametru
    # )

    roomID = (
        "roomID",
        "Podaj #ID pokoju"
    )
    roomNumber = (
        "roomNumber",
        "Podaj numer pokoju",
    )
    roomSize = (
        "roomSize",
        "Podaj rozmiar pokoju",
    )
    costPerDay = (
        "costPerDay",
        "Podaj cenę za jedną noc wynajęcia pokoju (np. 49.99)"
    )

    reservationID = (
        "reservationID",
        "Podaj #ID rezerwacji"
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

    # wyświetlenie tekstowej zachęty
    def text(self):
        return self.description + ": "
