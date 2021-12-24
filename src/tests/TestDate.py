import unittest
from classes.Date import Date
from definitions.ObjectStatus import ObjectStatus


class TestDate(unittest.TestCase):
    def test_1(self):
        date = Date('21.01.2022')
        self.assertEqual(str(date), '21.1.2022')
        self.assertEqual(date.objectStatus, ObjectStatus.Ok)

    def test_2(self):
        date = Date('21.11.2022')
        self.assertEqual(str(date), '21.11.2022')
        self.assertEqual(date.objectStatus, ObjectStatus.Ok)

    def test_3(self):
        date = Date('21.13.2022')
        self.assertEqual(date.objectStatus, ObjectStatus.Forbidden,
                         'Niedozwolona data nieobsłużona')

    def test_4(self):
        date = Date('41.1.2022')
        self.assertEqual(date.objectStatus, ObjectStatus.Forbidden,
                         'Niedozwolona data nieobsłużona')

    def test_5(self):
        date = Date('31.02.2022')
        self.assertEqual(date.objectStatus, ObjectStatus.Forbidden,
                         'Niedozwolona data nieobsłużona')

    def test_6(self):
        date = Date('05.01.2022')
        self.assertEqual(str(date), '5.1.2022')
        self.assertEqual(date.objectStatus, ObjectStatus.Ok)

    def test_7(self):
        date = Date('01.10.2022')
        self.assertEqual(str(date), '1.10.2022')
        self.assertEqual(date.objectStatus, ObjectStatus.Ok)