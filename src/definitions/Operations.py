from enum import Enum
from definitions.Params import Params
import storage


class Operations(Enum):
    # definicje wszystkich dostępnych operacji wykonywanych przez użytkownika w aplikacji

    # przykładowa operacja = (
    #     identyfikator operacji: "przykładowa operacja",
    #     "opis operacji",
    #     lista parametrów: [parametr1, parametr2],
    #     akcja z klasy Store, która ma zostać wywołana
    # )

    addRoom = (
        "addRoom",
        "Dodaj pokój",
        [Params.roomNumber, Params.roomSize],
        storage.rooms.add
    )
    modifyRoom = (
        "modifyRoom",
        "Zmodyfikuj pokój",
        [Params.roomID, Params.roomNumber, Params.roomSize],
        storage.rooms.modify
    )
    removeRoom = (
        "removeRoom",
        "Usuń pokój",
        [Params.roomID],
        storage.rooms.remove
    )
    listRooms = (
        "listRooms",
        "Wyświetl listę pokoi",
        [],
        storage.rooms.listElements
    )

    addReservation = (
        "addReservation",
        "Utwórz rezerwację",
        [Params.roomID, Params.reservationStart, Params.reservationEnd],
        storage.reservations.add
    )
    listReservations = (
        "listReservations",
        "Wyświetl listę rezerwacji",
        [],
        storage.reservations.listElements
    )

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _, description, params, run):
        self.description = description
        self.params = params
        self.run = run
        # self.actors = actors

    # wyświetlenie pozycji w menu
    def menuOption(self):
        print(self.value + ': ' + self.description)
