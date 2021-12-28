# todo weryfikacja poprawności daty
from definitions.ObjectStatus import ObjectStatus


class Date:
    # własna implementacja podstawowego obiektu daty
    # możliwe operacje porównania dat: <, <=, >=
    def __init__(self, dateString):
        # format zmiennej dateString: DD.MM.RRRR
        date = dateString.split('.')
        self.day = int(date[0])
        self.month = int(date[1])
        self.year = int(date[2])
        self.objectStatus = ObjectStatus.Ok

    # konwersja daty do integera na potrzeby porównywania
    def __int__(self):
        return self.day + self.month * 100 + self.year * 10000

    def __lt__(self, other):
        return int(self) < int(other)

    def __le__(self, other):
        return int(self) <= int(other)

    def __ge__(self, other):
        return int(self) >= int(other)

    def __str__(self):
        return str(self.day) + '.' + str(self.month) + '.' + str(self.year)
