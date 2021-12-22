import storage
from classes.Store import Store
from classes.Room import Room
from classes.Reservation import Reservation


def init():
    # przygotowanie magazynu danych
    storage.rooms = Store(Room)
    storage.reservations = Store(Reservation)
    # storage.services = Store(Services)


def main():
    from definitions.Operations import Operations

    # funkcja nasłuchująca operacji od użytkownika
    def listener():

        while True:

            # wypisz dostępne operacje
            print()
            for operation in Operations:
                operation.menuOption()

            operation = input()

            # operacja nie istnieje
            if not hasattr(Operations, operation):
                print('Niepoprawna nazwa operacji')
                continue

            operation = Operations[operation]

            n = len(operation.params)
            params = [None for _ in range(n)]

            # zebranie niezbędnych parametrów operacji
            for i in range(n):
                param = operation.params[i]
                params[i] = input(param.text())

            operation.run(params)

            # todo zaawansowana weryfikacja i obsługa błędów
            # try:
            #     operation.run(params)
            # except:
            #     print("Problem occurred")

    # todo runtests()

    listener()


init()
main()
