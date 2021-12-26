from definitions.ObjectStatus import ObjectStatus
from definitions.AccomodationStatus import AccomodationStatus
from definitions.PaymentStatus import PaymentStatus
import storage
from classes.Date import Date


class Reservation():
    # params = [roomKey, startString, endString]
    def __init__(self, key, params):
        self.key = key
        # klucz pokoju przypisanego do tej rezerwacji
        self.roomKey = int(params[0])
        self.objectStatus = ObjectStatus.Ok

        self.start = Date(params[1])
        self.end = Date(params[2])
        self.accomodationStatus = AccomodationStatus.Reserved
        self.paymentStatus = PaymentStatus.Unpaid
        self.name = str(params[3])
        self.surname = str(params[4])
        self.pesel = str(params[5])
        self.phone = str(params[6])

        # weryfikacja dostępności pokoju
        room = storage.rooms.get(self.roomKey)
        if not room.checkAvailability(self.start, self.end):
            print('Pokój niedostępny w tym terminie')
            self.objectStatus = ObjectStatus.Forbidden
        else:
            room.addReservation(self.key)

    def getAccomodationStatus(self):
        if self.accomodationStatus == AccomodationStatus.Reserved:
            return 'zarezerwowana'
        elif self.accomodationStatus == AccomodationStatus.Canceled:
            return 'anulowana'
        elif self.accomodationStatus == AccomodationStatus.Accommodated:
            return 'zakwaterowanie'
        elif self.accomodationStatus == AccomodationStatus.Ended:
            return 'zakończona'
       

    def __str__(self):
        return '#' + str(self.key) + ' pokój #' + str(self.roomKey) + ', ' + str(self.start) + '-' + str(self.end) +  ', status ' + self.getAccomodationStatus() + ', dane gościa: ' + str(self.name) + ' '  + str(self.surname) + ', nr PESEL: ' + str(self.pesel) + ', nr telefonu: ' + str(self.phone)

    def cancelReservation(self):
        self.accomodationStatus = AccomodationStatus.Canceled


    def accomodation(self):
        print("Weryfikacja tożsamości")
        newName = input("Podaj imię: ")
        newSurname = input("Podaj nazwisko: ")
        newPesel = input("Podaj numer pesel: ")

        if newName == self.name and newSurname == self.surname and newPesel == self.pesel:
            self.accomodationStatus = AccomodationStatus.Accommodated
            print("Zameldowano")
        else:
            print("Tożsamość nie została potwierdzona")



        
   

            
