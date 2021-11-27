from Date import Date

class Reservation():
    def __init__(self, params):
        self.room = str(params[2])
        self.start = Date(params[3])
        self.end = Date(params[4])
        
        self.accomodationStatus = 'reserved'
        self.paymentStatus = False