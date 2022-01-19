from enum import Enum
from helpers.correctData import *


class Params(Enum):
    # definicje wszystkich możliwych parametrów podawanych przez użytkownika w aplikacji

    # przykładowy parametr = (
    #     identyfikator parametru: 'przykładowy parametr',
    #     opis parametru,
    #     funkcja sprawdzająca poprawność parametru
    # )

    roomID = (
        'roomID',
        'Podaj #ID pokoju',
        correctRoomID,
    )
    roomNumber = (
        'roomNumber',
        'Podaj numer pokoju',
        correctRoomNumber,
    )
    roomSize = (
        'roomSize',
        'Podaj rozmiar pokoju - maksymalnie 5 osobowy',
        correctRoomSize,
    )
    costPerDay = (
        'costPerDay',
        'Podaj cenę za jedną noc wynajęcia pokoju (np. 49.99)',
        correctCostPerDay,
    )

    standard = (
        'standard',
        'Podaj standard pokoju (*, **, lub ***)',
        correctStandard,
    )

    reservationID = (
        'reservationID',
        'Podaj #ID rezerwacji',
        correctReservationID,
    )
    reservationStart = (
        'reservationStart',
        'Podaj datę początku rezerwacji [DD.MM.RRRR]',
        correctDate,
    )
    reservationEnd = (
        'reservationEnd',
        'Podaj datę końca rezerwacji [DD.MM.RRRR]',
        correctDate,
    )

    name = (
        'name',
        'Podaj imię',
        correctName,
    )

    surname = (
        'surname',
        'Podaj nazwisko',
        correctSurname,
    )

    pesel = (
        'pesel',
        'Podaj numer PESEL',
        correctPesel,
    )

    phone = (
        'phone',
        'Podaj numer telefonu',
        correctPhone,
    )

    paymentMethods = (
        'paymentMethod',
        'Wybierz metodę płatności [gotówka, karta, telefon, BLIK]',
        correctPaymentMethod,
    )

    description = (
        'description',
        'Podaj opis usługi',
        correctString,
    )
   
    time = (
        'time',
        'Podaj datę i godzinę',
        correctDateHour,
    )

    serviceID = (
        'serviceID',
        'Podaj ID usługi',
        correctServiceID,
        )

    

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _, description, isCorrect):
        self.description = description
        self.isCorrect = isCorrect

    # wyświetlenie tekstowej zachęty
    def text(self):
        return f'{self.description}: '
