from helpers.dateIntervalsDivergent import dateIntervalsDivergent
from classes.Date import Date
import storage


class Room():
    # params = [number, size, standard, costPerDay]
    def __init__(self, key, params):
        self.key = key
        # lista kluczy rezerwacji przypisanych do tego pokoju
        self.reservations = []
        self.objectStatus = 'ok'

        self.number = int(params[0])
        self.size = int(params[1])
        # self.standard = str(params[2])
        # self.costPerDay = float(params[3])

    def __str__(self):
        return '#' + str(self.key) + ' Room number ' + str(self.number) + ', size ' + str(self.size)

    # czy pokój jest dostępny w zadanym przedziale czasowym
    def checkAvailability(self, start: Date, end: Date):
        for reservationKey in self.reservations:
            reservation = storage.reservations.get(reservationKey)
            if not dateIntervalsDivergent(start, end, reservation.start, reservation.end):
                return False
        return True

    def addReservation(self, reservationKey):
        self.reservations.append(reservationKey)
