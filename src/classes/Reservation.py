import storage
from classes.Date import Date


class Reservation():
    # params = [roomKey, startString, endString]
    def __init__(self, key, params):
        self.key = key
        self.roomKey = int(params[0])
        self.objectStatus = 'ok'

        self.start = Date(params[1])
        self.end = Date(params[2])
        self.accomodationStatus = 'reserved'
        self.paymentStatus = False
        # self.name = str(params[3])
        # self.surname = str(params[4])
        # self.pesel = str(params[5])
        # self.phone = str(params[6])

        room = storage.rooms.get(self.roomKey)
        if not room.checkAvailability(self.start, self.end):
            print('Pokój niedostępny w tym terminie')
            self.objectStatus = 'forbidden'
        else:
            room.addReservation(self.key)

    def __str__(self):
        return '#' + str(self.key) + ' pokój #' + str(self.roomKey) + ', ' + str(self.start) + '-' + str(self.end)
