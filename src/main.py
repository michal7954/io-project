import storage
from classes.Store import Store
from classes.Room import Room
from classes.Reservation import Reservation


def init():
    storage.rooms = Store(Room)
    storage.reservations = Store(Reservation)
    # storage.services = Store(Services)


def main():
    from definitions.Operations import Operations

    def listener():

        while True:

            print()
            for operation in Operations:
                operation.menuOption()

            operation = input()

            if not hasattr(Operations, operation):
                print('Niepoprawna nazwa operacji')
                continue

            operation = Operations[operation]

            n = len(operation.params)
            params = [None for _ in range(n)]

            for i in range(n):
                param = operation.params[i]
                params[i] = input(param.text())

            operation.run(params)

            # todo zaawansowana weryfikacja i obsługa błędów
            # try:
            #     operation.call(params)
            # except:
            #     print("Problem occurred")

    # todo runtests()

    listener()


init()
main()
