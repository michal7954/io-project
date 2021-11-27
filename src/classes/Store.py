class Store():
    def __init__(self, Template):
        self.elements = {}
        self.nextKey=0
        self.Template = Template

    def generateKey(self):
        key = self.nextKey
        self.nextKey+=1
        return key

    def prepareObject(self, params):
        return self.Template(params)

    def call(self, params):
        operator = params[1]
        if operator=='add':
            element = self.prepareObject(params[2:])
            self.add(element)

        elif operator=='rem':
            key = int(params[2])
            self.rem(key)

        elif operator=='mod':
            key = int(params[2])
            element = self.prepareObject(params[3:])
            self.mod(key, element)

        elif operator=='get':
            key = int(params[2])
            self.get(key)

        elif operator=='list':
            self.listElements()

    def add(self, element):
        key = self.generateKey()
        self.elements[key]=element
        return key

    def rem(self, key):
        self.elements.pop(key)

    def mod(self, key, element):
        self.elements[key]=element

    def get(self, key):
        print(self.elements.get(key))

    def listElements(self):
        for key, element in self.elements.items():
            string = '#' + str(key) + ' ' + str(element)
            print(string)
