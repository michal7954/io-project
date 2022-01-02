from definitions.AccomodationStatus import AccomodationStatus
from definitions.ObjectStatus import ObjectStatus
from helpers.dateIntervalsDivergent import dateIntervalsDivergent
from classes.Date import Date
import storage


class Room():
    # params = [number, size, costPerDay, standard]
    def __init__(self, key, params):
        self.key = key
        # lista kluczy rezerwacji przypisanych do tego pokoju
        self.reservations = []
        self.objectStatus = ObjectStatus.Ok

        self.number = int(params[0])
        self.size = int(params[1])
        self.costPerDay = float(params[2])
        # self.standard = str(params[3])

    def __str__(self):
        return f'#{self.key} Pokój numer {self.number}, miejsc {self.size}, koszt {self.costPerDay:.2f}'

    # czy pokój jest dostępny w zadanym przedziale czasowym
    def checkAvailability(self, start: Date, end: Date):
        for reservationKey in self.reservations:
            reservation = storage.reservations.get(reservationKey)
            if reservation.accomodationStatus == AccomodationStatus.Canceled:
                continue
            if not dateIntervalsDivergent(start, end, reservation.start, reservation.end):
                return False
        return True

    def addReservation(self, reservationKey):
        self.reservations.append(reservationKey)
