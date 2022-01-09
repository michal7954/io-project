import unittest
from classes.Reservation import Reservation
from definitions.AccomodationStatus import AccomodationStatus
from definitions.ObjectStatus import ObjectStatus
from definitions.PaymentStatus import PaymentStatus
from helpers.initStorage import initStorage
from helpers.initData import initData


class TestReservation(unittest.TestCase):
    def setUp(self):
        initStorage()
        initData()

    def test_1(self):
        reservation = Reservation(
            101,
            [2, '3.1.2022', '9.1.2022','Adam','Kowal','12345678910','123456789']
        )
        self.assertEqual(reservation.objectStatus, ObjectStatus.Ok)
        self.assertEqual(reservation.accomodationStatus,
                         AccomodationStatus.Reserved)

    def test_2(self):
        reservation = Reservation(
            101,
            [2, '16.1.2022', '20.1.2022','Adam','Kowal','12345678910','123456789']
        )
        self.assertEqual(reservation.objectStatus, ObjectStatus.Ok)
        self.assertEqual(reservation.accomodationStatus,
                         AccomodationStatus.Reserved)

    def test_3(self):
        reservation = Reservation(
            101,
            [2, '3.1.2022', '3.1.2022','Adam','Kowal','12345678910','123456789']
        )
        self.assertEqual(reservation.objectStatus, ObjectStatus.Forbidden,
                         'Błędny przedział czasowy nieobsłużony')

    def test_4(self):
        reservation = Reservation(
            101,
            [2, '3.1.2022', '1.1.2022','Adam','Kowal','12345678910','123456789']
        )
        self.assertEqual(reservation.objectStatus, ObjectStatus.Forbidden,
                         'Błędny przedział czasowy nieobsłużony')

    def test_5(self):
        reservation = Reservation(
            101,
            [2, '3.1.2022', '43.1.2022','Adam','Kowal','12345678910','123456789']
        )
        self.assertEqual(reservation.objectStatus,
                         ObjectStatus.Forbidden, 'Niedozwolona data nieobsłużona')

    def test_6(self):
        reservation = Reservation(
            101,
            [2, '3.1.2022', '9.1.2022','Adam','Kowal','12345678910','123456789']
        )
        reservation.cancelReservation()
        self.assertEqual(reservation.objectStatus, ObjectStatus.Ok)
        self.assertEqual(reservation.accomodationStatus,
                         AccomodationStatus.Canceled)

    def test_7(self):
        reservation = Reservation(
            101,
            [3, '3.1.2022', '9.1.2022','Adam','Kowal','12345678910','123456789']
        )
        reservation.accommodate(['Adam','Kowal','12345678910'])
        self.assertEqual(reservation.objectStatus, ObjectStatus.Ok)
        self.assertEqual(reservation.accomodationStatus,
                         AccomodationStatus.Accommodated, 'Błąd oznaczania zameldowania')

    def test_8(self):
        reservation = Reservation(
            101,
            [3, '3.1.2022', '9.1.2022','Adam','Kowal','12345678910','123456789']
        )

        reservation.accommodate(['Adam','Kowal','12345678910'])
        reservation.checkOut(['Adam','Kowal','12345678910'])
        self.assertEqual(reservation.objectStatus, ObjectStatus.Ok)
        self.assertEqual(reservation.accomodationStatus,
                         AccomodationStatus.Accommodated, 'Błąd oznaczania zakończenia rezerwacji')

    def test_9(self):
        reservation = Reservation(
            101,
            [3, '3.1.2022', '9.1.2022','Adam','Kowal','12345678910','123456789']
        )
        reservation.checkOut(['Adam','Kowal','12345678910'])
        self.assertEqual(reservation.objectStatus, ObjectStatus.Ok)
        self.assertEqual(reservation.accomodationStatus, AccomodationStatus.Reserved,
                         'Nieobsłużony wyjątek wymeldowania przed zameldowaniem')

    def test_10(self):
        reservation = Reservation(
            101,
            [3, '3.1.2022', '9.1.2022','Adam','Kowal','12345678910','123456789']
        )
        reservation.markPaid([3,'BLIK'])
        self.assertEqual(reservation.objectStatus, ObjectStatus.Ok)
        self.assertEqual(reservation.paymentStatus, PaymentStatus.Paid,
                         'Błąd oznaczania rezerwacji opłaconej')

    # def test_11(self):
    #     reservation = Reservation(
    #         101,
    #         [3, '3.1.2022', '9.1.2022','Adam','Kowal','12345678910','123456789']
    #     )
    #     reservation.setDeferred()
    #     self.assertEqual(reservation.objectStatus, ObjectStatus.Ok)
    #     self.assertEqual(reservation.paymentStatus, PaymentStatus.Deferred,
    #                      'Błąd oznaczania rezerwacji odroczonej')
                        
    def test_12(self):
        reservation = Reservation(
            101,
            [3, '16.1.2022', '25.1.2022','Adam','Kowal','12345678910','123456789']
        )
        self.assertEqual(reservation.objectStatus, ObjectStatus.Ok)
        self.assertEqual(reservation.accomodationStatus,
                         AccomodationStatus.Reserved)

    def test_13(self):
        reservation = Reservation(
            101,
            [5, '1.1.2022', '10.1.2022','Adam','Kowal','12345678910','123456789']
        )
        self.assertEqual(reservation.objectStatus, ObjectStatus.Ok)
        self.assertEqual(reservation.accomodationStatus,
                         AccomodationStatus.Reserved)

    def test_14(self):
        reservation = Reservation(
            101,
            [4, '6.1.2022', '10.1.2022','Adam','Kowal','12345678910','123456789']
        )
        self.assertEqual(reservation.objectStatus, ObjectStatus.Ok)
        self.assertEqual(reservation.accomodationStatus,
                         AccomodationStatus.Reserved)

    def test_15(self):
        reservation = Reservation(
            101,
            [8, '1.1.2022', '31.1.2022','Adam','Kowal','12345678910','123456789']
        )
        self.assertEqual(reservation.objectStatus, ObjectStatus.Ok)
        self.assertEqual(reservation.accomodationStatus,
                         AccomodationStatus.Reserved)

    def test_16(self):
        reservation = Reservation(
            101,
            [2, '3.1.2022', '9.1.2022','adam','Kowal','12345678910','123456789']
        )
        self.assertEqual(reservation.objectStatus, ObjectStatus.Forbidden,
                         'Błędne Imię')


    def test_17(self):
        reservation = Reservation(
            101,
            [2, '16.1.2022', '20.1.2022','Adam','123','12345678910','123456789']
        )
        self.assertEqual(reservation.objectStatus, ObjectStatus.Forbidden,
                         'Błędne Nazwisko')


    def test_18(self):
        reservation = Reservation(
            101,
            [2, '3.1.2022', '3.1.2022','Adam','Kowal','123456789109','123456789']
        )
        self.assertEqual(reservation.objectStatus, ObjectStatus.Forbidden,
                         'Błędny PESEL')

    def test_19(self):
        reservation = Reservation(
            101,
            [2, '3.1.2022', '1.1.2022','Adam','Kowal','12345678910','+123456789']
        )
        self.assertEqual(reservation.objectStatus, ObjectStatus.Forbidden,
                         'Błędny telefon')