import storage
from classes.Store import Store
from classes.Room import Room
from classes.Reservation import Reservation


def main():
    global storage

    storage.rooms = Store(Room)
    storage.reservations = Store(Reservation)
    # storage.services = Store(Services)

    def listener():

        while True:
            line = input()
            params = line.split()

            if len(params) == 0:
                continue

            store = params[0]
            if store == 'rooms':
                store = storage.rooms
            elif store == 'reservations':
                store = storage.reservations
            # elif store == 'services':
            #     store = storage.services

            store.call(params)

            # todo zaawansowana weryfikacja i obsługa błędów
            # try:
            #     store.call(params)
            # except:
            #     print("Problem occurred")

    # todo runtests()

    listener()


main()
