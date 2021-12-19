class Store():
    def __init__(self, ClassTemplate):
        self.elements = {}
        self.nextKey = 1
        self.ClassTemplate = ClassTemplate

    def generateKey(self):
        key = self.nextKey
        self.nextKey += 1
        return key

    def prepareObject(self, key, params):
        element = self.ClassTemplate(key, params)
        if element.objectStatus == 'ok':
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
            print(str(element))
