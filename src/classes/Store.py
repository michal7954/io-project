class Store():
    def __init__(self, Template):
        self.elements = {}
        self.nextKey = 1
        self.Template = Template

    def generateKey(self):
        key = self.nextKey
        self.nextKey += 1
        return key

    def prepareObject(self, key, params):
        element = self.Template(key, params)
        if element.objectStatus == 'ok':
            return element
        print('Object creation error')
        return None

    def call(self, params):
        operator = params[1]

        if operator == 'add':
            self.add(params)
        elif operator == 'rem':
            self.remove(params)
        elif operator == 'mod':
            self.modify(params)
        elif operator == 'get':
            key = int(params[2])
            self.get(key)
        elif operator == 'list':
            self.listElements()

    def add(self, params):
        key = self.generateKey()
        element = self.prepareObject(key, params[2:])
        if element:
            self.elements[key] = element
            return key

    def modify(self, params):
        key = int(params[2])
        element = self.prepareObject(key, params[3:])
        if element:
            self.elements[key] = element
            return key

    def remove(self, params):
        key = int(params[2])
        self.elements.pop(key)

    def get(self, key):
        return self.elements.get(key)

    def listElements(self):
        for element in self.elements.values():
            print(str(element))
