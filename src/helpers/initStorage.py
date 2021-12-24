import storage
from classes.Store import Store
from classes.Room import Room
from classes.Reservation import Reservation


def initStorage():
    storage.rooms = Store(Room)
    storage.reservations = Store(Reservation)
    # storage.services = Store(Services)
