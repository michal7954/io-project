from enum import Enum
from definitions.Operations import Operations


class Users(Enum):
    # definicje oprawnień użytkowników do wykonywania poszczególnych operacji

    # przykładowy użytkownik systemu = (
    #     identyfikator użytkownika: 'przykładowy użytkownik systemu',
    #     'opis użytkownika',
    #     lista dozwolonych operacji: [
    #           operacja1,
    #           operacja2
    #     ],
    # )

    user = (
        'user',
        'Potencjalny gość hotelu',
        [
            Operations.listRooms,
            Operations.addReservation,
            Operations.cancelReservation,
            Operations.findAvailable,
            Operations.logout
        ],
    )

    guest = (
        'guest',
        'Gość hotelu',
        [
            Operations.orderTide,
            Operations.orderBreakfast,
            Operations.orderConservator,
            Operations.logout
        ],
    )

    receptionist = (
        'receptionist',
        'Pracownik recepcji hotelu',
        [
            Operations.listRooms,
            Operations.addReservation,
            Operations.listReservations,
            Operations.cancelReservation,
            Operations.accommodate,
            Operations.checkOut,
            Operations.pay,
            Operations.checkPaymentStatus,
            Operations.listServices,
            Operations.findAvailable,
            Operations.setDone,
            Operations.logout
        ],
    )

    manager = (
        'manager',
        'Menedżer hotelu / administrator systemu',
        [
            Operations.addRoom,
            Operations.modifyRoom,
            Operations.removeRoom,
            Operations.listRooms,
            Operations.listReservations,
            Operations.listServices,
            Operations.logout
        ],
    )

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _, description, operations):
        self.description = description
        self.operations = operations

    # wyświetlenie pozycji w menu
    def getMenuOption(self):
        return f'{self.value}: {self.description}'
