import unittest
from classes.Date import Date
from definitions.ObjectStatus import ObjectStatus
from helpers.initStorage import initStorage
from helpers.initData import initData
import storage
from io import StringIO
import sys


class TestStore(unittest.TestCase):
    def setUp(self):
        initStorage()
        initData()

    def test_1(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        storage.rooms.findAvailable(['2.1.2022', '3.1.2022'])
        sys.stdout = sys.__stdout__
        resultsNumber = capturedOutput.getvalue().count('\n')
        self.assertEqual(resultsNumber, 16)

    def test_2(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        storage.rooms.findAvailable(['1.1.2022', '31.1.2022'])
        sys.stdout = sys.__stdout__
        resultsNumber = capturedOutput.getvalue().count('\n')
        self.assertEqual(resultsNumber, 15)

    def test_3(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        storage.rooms.listElements(None)
        sys.stdout = sys.__stdout__
        resultsNumber = capturedOutput.getvalue().count('\n')
        self.assertEqual(resultsNumber, 19)

    def test_4(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        storage.reservations.listElements(None)
        sys.stdout = sys.__stdout__
        resultsNumber = capturedOutput.getvalue().count('\n')
        self.assertEqual(resultsNumber, 15)