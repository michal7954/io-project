import unittest
from classes.Service import Service
from definitions.ServiceStatus import ServiceStatus
from definitions.ObjectStatus import ObjectStatus
from helpers.initStorage import initStorage
from helpers.initData import initData


class TestService(unittest.TestCase):
    def setUp(self):
        initStorage()
        initData()

    def test_1(self):
        service = Service(
            101,
            # [typ, ID rezerwacji, opis, termin]
            ['breakfast', 2, '', '4.1.2022 10:00']
        )
        self.assertEqual(service.objectStatus, ObjectStatus.Ok)
        self.assertEqual(service.serviceStatus, ServiceStatus.Pending)

    def test_2(self):
        service = Service(
            101,
            ['breakfast', 3, '', '7.1.2022 9:00']
        )
        self.assertEqual(service.objectStatus, ObjectStatus.Ok)
        self.assertEqual(service.serviceStatus, ServiceStatus.Pending)

    def test_3(self):
        service = Service(
            101,
            ['breakfast', 3, '', '8.1.2022 10:15']
        )
        service.setDone()
        self.assertEqual(service.objectStatus, ObjectStatus.Ok)
        self.assertEqual(service.serviceStatus, ServiceStatus.Done,
                         'Błąd oznaczenia wykonania usługi')

    def test_4(self):
        service = Service(
            101,
            ['breakfast', 3, '', '6.1.2022 8:30']
        )
        self.assertEqual(service.objectStatus, ObjectStatus.Forbidden,
                         'Niedozwolony czas wykonania usługi nieobsłużony')

    def test_5(self):
        service = Service(
            101,
            ['breakfast', 3, '', '10.1.2022 9:00']
        )
        self.assertEqual(service.objectStatus, ObjectStatus.Forbidden,
                         'Niedozwolony czas wykonania usługi nieobsłużony')
