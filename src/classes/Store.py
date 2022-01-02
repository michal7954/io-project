from definitions.ObjectStatus import ObjectStatus


class Store():
    # MagazynDanych odpowiada za przechowywanie listy rekordów jednego z typów
    def __init__(self, ClassTemplate):
        # dane są przechowywane w asocjacyjnej strukturze słownika
        self.elements = {}
        self.nextKey = 1
        # typ przechowywanych elementów (Room/Reservation/Service)
        self.ClassTemplate = ClassTemplate

    # magazyn ma zaimplementowaną funkcję zarządzania kluczami w oparciu o nextKey
    def generateKey(self):
        key = self.nextKey
        self.nextKey += 1
        return key

    def prepareObject(self, key, params):
        # wywołanie konstruktora klasy potomnej
        element = self.ClassTemplate(key, params)
        if element.objectStatus == ObjectStatus.Ok:
            return element
        print('Błąd tworzenia obiektu')
        return None

    def add(self, params):
        key = self.generateKey()
        element = self.prepareObject(key, params)
        if element:
            self.elements[key] = element
            return key

    def modify(self, params):
        key = int(params[0])
        element = self.prepareObject(key, params[1:])
        if element:
            self.elements[key] = element
            return key

    def remove(self, params):
        key = int(params[0])
        self.elements.pop(key)

    def get(self, key):
        return self.elements.get(key)

    def listElements(self, _):
        for element in self.elements.values():
            print(element)
