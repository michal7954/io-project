import storage
from classes.Store import Store
from classes.Room import Room
from classes.Reservation import Reservation
from helpers.initData import initData


def initStorage():
    storage.rooms = Store(Room)
    storage.reservations = Store(Reservation)
    # storage.services = Store(Services)


def main():
    # przygotowanie magazynu danych
    initStorage()

    # wypełnienie magazynu przykładowymi danymi
    initData()

    from definitions.Operations import Operations

    def listener():
        # funkcja nasłuchująca operacji od użytkownika

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
            # except Exception as e:
            #     print('Wystąpił problem')
            #     print(e)

    listener()


main()
