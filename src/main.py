from helpers.initStorage import initStorage
from helpers.initData import initData
from helpers.systemOperations import listener


def main():
    # przygotowanie magazynu danych
    initStorage()

    # wypełnienie magazynu przykładowymi danymi
    initData()

    # pętla nasłuchująca na operacje wprowadzane przez użytkownika
    listener()


if __name__ == '__main__':
    main()
