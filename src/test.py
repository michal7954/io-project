import unittest
from tests.TestDate import TestDate
from tests.TestReservation import TestReservation
from tests.TestService import TestService
from tests.TestRoom import TestRoom
from tests.TestStore import TestStore


# aby uruchomić testy należy przejść do lokalicacji io-project\src i wywołać
# py -m unittest test
# zamiast 'test' można precyzować poszczególne moduły, np. test.TestDate
# albo adresować konkretne testCasy, np. test.TestDate.test_1

# alternatywne można uruchomić wszystkie testy przez wykonanie pliku test.py
if __name__ == '__main__':
    unittest.main()
