from definitions.ObjectStatus import ObjectStatus
from definitions.AccomodationStatus import AccomodationStatus
from definitions.PaymentStatus import PaymentStatus
from definitions.PaymentMethod import PaymentMethod
import storage
from classes.Date import Date
from helpers.numberOfDays import numberOfDays
from helpers.correctData import correctReservation


class Reservation():
    # params = [roomKey, startString, endString]
    def __init__(self, key, params):
        if correctReservation(params):
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
                print('\tPokój niedostępny w tym terminie')
                self.objectStatus = ObjectStatus.Forbidden
            else:
                room.addReservation(self.key)
        else:
            self.objectStatus = ObjectStatus.Forbidden

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
        return f'#{self.key} pokój #{self.roomKey}, {self.start}-{self.end}, status {self.getAccomodationStatus()}, dane gościa: {self.name} {self.surname}, PESEL: {self.pesel}, tel.: {self.phone}'

    def cancelReservation(self):
        self.accomodationStatus = AccomodationStatus.Canceled
        print('\tRezerwacja anulowana')

    def accommodate(self, params):
        # Sprawdzamy czy dane wprowadzone przy rezerwacji zgadają się z tymi podanymi przy zameldowaniu
        if params[0] == self.name and params[1] == self.surname and params[2] == self.pesel:
            self.accomodationStatus = AccomodationStatus.Accommodated
            print('\tZameldowano')
        else:
            print('\tTożsamość nie została potwierdzona')

    # Wymeldowanie
    def checkOut(self, params):
        if self.accomodationStatus == AccomodationStatus.Accommodated:
            if params[0] == self.name and params[1] == self.surname and params[2] == self.pesel:
                if self.paymentStatus == PaymentStatus.Paid:
                    self.accomodationStatus = AccomodationStatus.Ended
                    print('\tWymeldowano')
                else:
                    print('\tNie uiszczono opłaty')
            else:
                print('\tTożsamość nie została potwierdzona')
        else:
            print('\tRezerwacja nie ma statusu zameldowania')

    # Sprawdzenie statusu płatności podanej rezerwacji (opłacona,odroczona,niepołacona)
    def checkPaymentStatus(self):
        if self.paymentStatus == PaymentStatus.Paid:
            print('\tRezerwacja opłacona')
        if self.paymentStatus == PaymentStatus.Deferred:
            print('\tPłatność odrocznona')
        if self.paymentStatus == PaymentStatus.Unpaid:
            print('\tRezerwacja nieopłacona')

    # Realizacja płatności i zmiana statusu
    def markPaid(self, params):
        if self.accomodationStatus == AccomodationStatus.Canceled or self.accomodationStatus == AccomodationStatus.Ended:
            print('\tRezerwacja nieaktualna')
            return
        if self.paymentStatus == PaymentStatus.Paid:
            print('\tRezerwacja opłacona')
            return

        # Zapisanie metody płatności
        method = params[1]
        if method == 'gotówka':
            self.paymentMethod = PaymentMethod.Cash
        if method == 'karta':
            self.paymentMethod = PaymentMethod.Card
        if method == 'telefon':
            self.paymentMethod = PaymentMethod.Phone
        if method == 'BLIK':
            self.paymentMethod = PaymentMethod.Blik

        # Obliczanie ceny pobytu
        room = storage.rooms.get(self.roomKey)
        number = numberOfDays(self.start, self.end)
        prize = room.costPerDay * number

        print(f'\tKoszt pobytu wynosi: {prize:.2f} zł')

        # Możliwość odroczenia płatności, przy pobycie dłuższym niż 5 dni
        if number > 5:
            print('\tPobyt wynosi więcej niż 5 dni\nPłatność może zostać zrealizowana podczas wymeldowania.')
            answer = ''
            while answer != 'TAK' and answer != 'NIE':
                answer = input('\tCzy chcesz odroczyć płatność? [TAK, NIE]: ')
                if answer == 'TAK':
                    self.paymentStatus = PaymentStatus.Deferred
                    print('\tPłatność odroczona')
                elif answer == 'NIE':
                    self.paymentStatus = PaymentStatus.Paid
                    print(f'\tZapłacono. Użyta metoda płatności: {method}')
                else:
                    print('\tBłędnie wprowadzona odpowiedź. Podaj [TAK, NIE]')
        else:
            self.paymentStatus = PaymentStatus.Paid
            print(f'\tZapłacono. Użyta metoda płatności: {method}')
