from definitions.AccomodationStatus import AccomodationStatus
from definitions.ObjectStatus import ObjectStatus
from definitions.ServiceStatus import ServiceStatus
from classes.Date import Date
import storage


class Service():
    # params [idRezerwacji, typ, opis, termin]

    def __init__(self, key, params):
        self.key = key
        # lista kluczy rezerwacji przypisanych do tego pokoju
        self.objectStatus = ObjectStatus.Ok
        self.serviceStatus = ServiceStatus.Pending
       
        self.type = str(params[0])
        self.reservationKey=int(params[1])
        self.description = str(params[2])
        self.time = str(params[3])

        reservation = storage.reservations.get(self.reservationKey)
        if reservation.accomodationStatus != AccomodationStatus.Accommodated:
            print('\tRezerwacja nie ma statusu zakwaterowania\n\tNie można wykonać usługi')
            self.objectStatus = ObjectStatus.Forbidden

        date = self.time.split(' ')
        if not (Date(date[0]) >= reservation.start and Date(date[0]) <= reservation.end):
            print('\tPodany czas usługi jest niezgodny z datą pobytu\n\tNie można wykonac usługi')
            self.objectStatus = ObjectStatus.Forbidden

    def __str__(self):
        if self.serviceStatus == ServiceStatus.Pending:
            status='niezrealizowana'
        else:
            status='zrealizowana'

        if self.type == 'breakfast':
            type='Śniadanie'
        elif self.type =='tide':
            type='Sprzątanie'
        else:
            type='Konserwator'

        return f'#{self.key} ID usługi: {self.key}, typ: '+type+f' ID rezerwacji: {self.reservationKey}, Opis: {self.description}, Termin: {self.time}, status: '+status

    # Sprawdzenie statusu wykonania podanej usługi
    def checkServiceStatus(self):
        if self.serviceStatus == ServiceStatus.Done:
            print('\tUsługa wykonana')
        if self.serviceStatus == ServiceStatus.Pending:
            print('\tUsługa w trakcie')

    def setDone(self):
        self.serviceStatus = ServiceStatus.Done
        print('\tUsługa wykonana')
