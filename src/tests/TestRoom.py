import unittest
from classes.Date import Date
from classes.Room import Room
from definitions.ObjectStatus import ObjectStatus
from helpers.initStorage import initStorage
from helpers.initData import initData
import storage


class TestRoom(unittest.TestCase):
    def setUp(self):
        initStorage()
        initData()

    def test_1(self):
        room = Room(
            101,
            ['1', '4', '32.30']
        )
        self.assertEqual(room.number, 1)
        self.assertEqual(room.size, 4)
        self.assertEqual(room.costPerDay, 32.3)
        self.assertEqual(room.objectStatus, ObjectStatus.Ok)

    def test_2(self):
        room = Room(
            101,
            ['wqer', 'qwer', 'qwer']
        )
        self.assertEqual(room.objectStatus, ObjectStatus.Forbidden,
                         'Nieobsłużony błędny typ danych')

    def test_3(self):
        room = Room(
            101,
            ['sdfa', '2', '3']
        )
        self.assertEqual(room.objectStatus, ObjectStatus.Forbidden,
                         'Nieobsłużony błędny typ danych')

    def test_4(self):
        room = Room(
            101,
            ['1', 'qwer', '3']
        )
        self.assertEqual(room.objectStatus, ObjectStatus.Forbidden,
                         'Nieobsłużony błędny typ danych')

    def test_5(self):
        room = Room(
            101,
            ['1', '2', 'qwer']
        )
        self.assertEqual(room.objectStatus, ObjectStatus.Forbidden,
                         'Nieobsłużony błędny typ danych')

    def test_6(self):
        room = storage.rooms.get(1)
        self.assertTrue(room.checkAvailability(
            Date('2.1.2022'), Date('3.1.2022')))

    def test_7(self):
        room = storage.rooms.get(1)
        self.assertFalse(room.checkAvailability(
            Date('2.1.2022'), Date('4.1.2022')))

    def test_8(self):
        room = storage.rooms.get(1)
        
        storage.reservations.get(2).cancelReservation()
        self.assertTrue(room.checkAvailability(
            Date('2.1.2022'), Date('4.1.2022')))

    def test_9(self):
        room = storage.rooms.get(1)

        self.assertFalse(room.checkAvailability(
            Date('2.1.2022'), Date('7.1.2022')))

        storage.reservations.get(2).cancelReservation()
        self.assertTrue(room.checkAvailability(
            Date('2.1.2022'), Date('7.1.2022')))
