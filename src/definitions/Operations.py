from enum import Enum
from definitions.Params import Params
from helpers.systemOperations import logout
import storage
from classes.Date import Date


class Operations(Enum):
    # definicje wszystkich dostępnych operacji wykonywanych przez użytkownika w aplikacji

    # przykładowa operacja = (
    #     identyfikator operacji: 'przykładowa operacja',
    #     'opis operacji',
    #     lista parametrów: [parametr1, parametr2],
    #     wskaźnik do metody lub funkcja anonimowa, która ma zostać wywołana
    # )

    addRoom = (
        'addRoom',
        'Dodaj pokój',
        [Params.roomNumber, Params.roomSize, Params.costPerDay, Params.standard],
        storage.rooms.add
    )
    modifyRoom = (
        'modifyRoom',
        'Zmodyfikuj pokój',
        [Params.roomID, Params.roomNumber, Params.roomSize, Params.costPerDay, Params.standard],
        storage.rooms.modify
    )
    removeRoom = (
        'removeRoom',
        'Usuń pokój',
        [Params.roomID],
        storage.rooms.remove
    )
    listRooms = (
        'listRooms',
        'Wyświetl listę pokoi',
        [],
        storage.rooms.listElements
    )

    addReservation = (
        'addReservation',
        'Utwórz rezerwację',
        [Params.roomID, Params.reservationStart, Params.reservationEnd, Params.name, Params.surname, Params.pesel, Params.phone],
        storage.reservations.add
    )
    listReservations = (
        'listReservations',
        'Wyświetl listę rezerwacji',
        [],
        storage.reservations.listElements
    )
    cancelReservation = (
        'cancelReservation',
        'Anuluj rezerwację',
        [Params.reservationID],
        lambda params: storage.reservations.get(int(params[0])).cancelReservation()
    )

    accommodate = (
        'accommodate',
        'Zamelduj',
        [Params.reservationID, 'Weryfikacja tożsamości', Params.name, Params.surname, Params.pesel],
        lambda params: storage.reservations.get(int(params[0])).accommodate(params[2:])
    )

    checkOut = (
        'checkOut',
        'Wymelduj',
        [Params.reservationID, 'Weryfikacja tożsamości', Params.name, Params.surname, Params.pesel],
        lambda params: storage.reservations.get(int(params[0])).checkOut(params[2:])
    )
    pay = (
        'pay',
        'Zapłać',
        [Params.reservationID, Params.paymentMethods],
        lambda params: storage.reservations.get(int(params[0])).markPaid(params)
    )

    checkPaymentStatus = (
        'checkPaymentStatus',
        'Sprawdź status płatności rezerwacji',
        [Params.reservationID],
        lambda params: storage.reservations.get(int(params[0])).checkPaymentStatus()
    )

    orderTide = (
        'orderTide',
        'Zamów sprzątanie pokoju',
        [Params.reservationID, Params.serviceComments, Params.serviceDeadline],
        lambda params: storage.services.add(['tide']+params)
    )

    orderBreakfast = (
        'orderBreakfast',
        'Zamów śniadanie do pokoju',
        [Params.reservationID, Params.serviceComments, Params.serviceDeadline],
        lambda params: storage.services.add(['breakfast']+params)
    )

    orderConservator = (
        'orderConservator',
        'Zamów konserwatora',
        [Params.reservationID, Params.serviceComments, Params.serviceDeadline],
        lambda params: storage.services.add(['conservator']+params)
    )

    listServices = (
        'listServices',
        'Wyświetl listę usług',
        [],
        storage.services.listElements
        )

    findAvailable = (
        'findAvailable',
        'Wyświetl pokoje dostępne w zadanym terminie',
        [Params.reservationStart, Params.reservationEnd],
        lambda params: storage.rooms.findAvailable(Date(params[0]),Date(params[1]))
    )
    setDone = (
        'setDone',
        'Oznacz usługę jako wykonaną',
        [Params.serviceID],
        lambda params: storage.services.get(int(params[0])).setDone()
        )

    logout = (
        'logout',
        'Wyloguj i wybierz nowego użytkownika',
        [],
        logout
    )

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _, description, params, run):
        self.description = description
        self.params = params
        self.run = run

    # wyświetlenie pozycji w menu
    def getMenuOption(self):
        return f'{self.value}: {self.description}'