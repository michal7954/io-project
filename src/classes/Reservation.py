from definitions.ObjectStatus import ObjectStatus
from definitions.AccomodationStatus import AccomodationStatus
from definitions.PaymentStatus import PaymentStatus
from definitions.PaymentMethod import PaymentMethod
import storage
from classes.Date import Date
from helpers.numberOfDays import numberOfDays
from time import sleep


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
        self.paymentMethod = PaymentMethod.NotChosen

        # weryfikacja dostępności pokoju
        room = storage.rooms.get(self.roomKey)
        if not room.checkAvailability(self.start, self.end):
            print(self.key)
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


    def accommodate(self,params):
        # Sprawdzamy czy dane wprowadzone przy rezerwacji zgadają się z tymi podanymi przy zameldowaniu
        if params[0]==self.name and params[1]==self.surname and params[2]==self.pesel:
            self.accomodationStatus = AccomodationStatus.Accommodated
            print('Zameldowano')
        else:
            print('Tożsamość nie została potwierdzona')

    # Wymeldowanie
    def checkOut(self, params):
        if params[0]==self.name and params[1]==self.surname and params[2]==self.pesel:
            if  self.paymentStatus == PaymentStatus.Paid:
                 self.accomodationStatus = AccomodationStatus.Ended
                 print('Wymeldowano. Dziękujemy za pobyt')
            else:
               print('Musisz dokonać płatności')
        else:
            print('Tożsamość nie została potwierdzona')

    # Sprawdzenie statusu płatności podanej rezerwacji (opłacona,odroczona,niepołacona)
    def checkPaymentStatus(self, _):
        if  self.paymentStatus == PaymentStatus.Paid:
            print('Rezerwacja opłacona')
        if  self.paymentStatus == PaymentStatus.Deferred:
            print('Płatność odrocznona')
        if  self.paymentStatus == PaymentStatus.Unpaid:
            print('Rezerwacja nieopłacona')
            
    # Realizacja płatności i zmiana statusu
    def markPaid(self, params):
        if self.accomodationStatus == AccomodationStatus.Canceled or self.accomodationStatus == AccomodationStatus.Ended:
            print('Rezerwacja nieaktualna')
            return
        if  self.paymentStatus == PaymentStatus.Paid:
            print('Rezerwacja opłacona')
            return

        # Zapisanie metody płatności
        if params=='gotówka':
            self.paymentMethod = PaymentMethod.Cash
        if params=='karta':
            self.paymentMethod = PaymentMethod.Card
        if params=='telefon':
            self.paymentMethod = PaymentMethod.Phone
        if params=='BLIK':
            self.paymentMethod = PaymentMethod.Blik
        
        # Obliczanie ceny pobytu 
        room = storage.rooms.get(self.roomKey)
        number = numberOfDays(self.start,self.end)
        prize = room.costPerDay * number

        print('Koszt pobytu wynosi: ', prize, ' zł')

        # Możliwość odroczenia płatności, przy pobycie dłuższym niż 5 dni
        if number > 5:
            print('Pobyt wynosi więcej niż 5 dni. Płatność może zostać zrealizowana podczas wymeldowania.')
            answer=''
            while answer!='TAK' and answer!='NIE':
                answer = input('Czy chcesz odroczyć płatność? [TAK,NIE]: ')
                if answer == 'TAK':
                    self.paymentStatus = PaymentStatus.Deferred
                    print('Płatność odroczona')
                elif answer == 'NIE':
                    self.paymentStatus = PaymentStatus.Paid
                    print('...')
                    sleep(3)
                    print('Zapłacono. Użyta metoda płatności: ', params)
                else:
                    print('Błędnie wprowadzona odpowiedź. Podaj "TAK" lub "NIE".')
        else:
            self.paymentStatus = PaymentStatus.Paid
            print('...')
            sleep(3)
            print('Zapłacono. Użyta metoda płatności: ', params)


        
   

            
