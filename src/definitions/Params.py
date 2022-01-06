from enum import Enum
from helpers.correctData import * 

class Params(Enum):
    # definicje wszystkich możliwych parametrów podawanych przez użytkownika w aplikacji

    # przykładowy parametr = (
    #     identyfikator parametru: 'przykładowy parametr',
    #     opis parametru
    # )

    roomID = (
        'roomID',
        'Podaj #ID pokoju',
        correctRoomID,
        'Błędnie wprowadzone ID pokoju'
    )
    roomNumber = (
        'roomNumber',
        'Podaj numer pokoju',
        correctRoomNumber,
        'Błędnie wprowadzony numer pokoju'
    )
    roomSize = (
        'roomSize',
        'Podaj rozmiar pokoju',
        correctRoomSize,
        'Błędnie wprowadzony rozmiar pokoju'

    )
    costPerDay = (
        'costPerDay',
        'Podaj cenę za jedną noc wynajęcia pokoju (np. 49.99)',
        correctCostPerDay,
        'Błędnie wprowadzony koszt pobytu'
    )

    standard = (
        'standard',
        'Podaj standard pokoju (*, **, lub ***)',
        correctStandard,
        'Błednie wprowadzony standard pokoju'
     )

    reservationID = (
        'reservationID',
        'Podaj #ID rezerwacji',
        correctReservationID,
        'Błednie wprowadzone ID rezerwacji'
    )
    reservationStart = (
        'reservationStart',
        'Podaj datę początku rezerwacji [DD.MM.RRRR]',
        correctDate,
        'Błędnie wprowadzona data'
    )
    reservationEnd = (
        'reservationEnd',
        'Podaj datę końca rezerwacji [DD.MM.RRRR]',
        correctDate,
        'Błędnie wprowadzona data'
    )

    name = (
        'name',
        'Podaj imię',
        correctName,
        'Błędnie wprowadzone imię'
    )

    surname = (
        'surname',
        'Podaj nazwisko',
        correctSurname,
        'Błędnie wprowadzone nazwisko'
    )

    pesel = (
        'pesel',
        'Podaj numer PESEL',
        correctPesel,
        'Błędnie wprowadzony PESEL'
    )

    phone = (
        'phone',
        'Podaj numer telefonu',
        correctPhone,
        'Błędnie wprowadzony numer telefonu'
    )

    paymentMethods = (
        'paymentMethod',
        'Wybierz metodę płatności [gotówka, karta, telefon, BLIK]',
        correctPaymentMethod,
        'Błędnie wprowadzona metoda płatności'
        )


    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _, description, isCorrect, errorComment):
        self.description = description
        self.isCorrect = isCorrect
        self.errorComment = errorComment

    # wyświetlenie tekstowej zachęty
    def text(self):
        return f'{self.description}: '
