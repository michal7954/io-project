class Room():
    def __init__(self, params):
        self.number = params[0]
        self.size = params[1]
        # self.standard = params[2]
        # self.costPerDay = params[3]

    def __str__(self):
        return 'Room number ' + str(self.number) + ', size ' + str(self.size)