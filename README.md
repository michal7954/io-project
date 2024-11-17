# Hotel Management System

## Project Description
This is a hotel management system built using object-oriented programming paradigm in Python. The system allows for managing hotel operations such as room reservations, service management, and record-keeping for various hotel-related activities. It is designed to handle core functionalities required for running a hotel smoothly and efficiently.

The implemented unit tests in this project verify the functionality and correctness of various classes and methods, including Date, Reservation, Room, Service, and Store.

## Key Use Cases
- **Room Management**: Add, modify, and remove hotel rooms. Check room availability for given dates.
- **Reservation Management**: Create, modify, and cancel reservations. Track reservation status and guest details.
- **Service Management**: Manage various services (e.g., breakfast, cleaning) associated with reservations.
- **Guest Management**: Maintain guest records, including personal details and stay history.
- **Payment Processing**: Handle payments and update the payment status for reservations.

## Code Highlights
### Store Class
The [Store](https://github.com/michal7954/io-project/blob/main/src/classes/Store.py) class is responsible for managing a collection of objects such as rooms, reservations, and services. It handles key generation, object preparation, and basic CRUD (Create, Read, Update, Delete) operations.
```python
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
        if element.objectStatus == ObjectStatus.Ok:
            return element
        return None

    def add(self, params):
        key = self.generateKey()
        element = self.prepareObject(key, params)
        if element:
            self.elements[key] = element
            print('\tOperation successful\n\tID: ', key)
            return key
```

### Room Class
The [Room](https://github.com/michal7954/io-project/blob/main/src/classes/Room.py) class manages room details and checks availability for given date ranges.
```python
class Room():
    def __init__(self, key, params):
        if correctRoom(params):
            self.key = key
            self.reservations = []
            self.objectStatus = ObjectStatus.Ok

            self.number = int(params[0])
            self.size = int(params[1])
            self.costPerDay = float(params[2])
            self.standard = str(params[3])
        else:
            self.objectStatus = ObjectStatus.Forbidden

    def __str__(self):
        return f'#{self.key} Room number {self.number}, size {self.size}, cost {self.costPerDay:.2f}, standard {self.standard}'

    def checkAvailability(self, start: Date, end: Date):
        for reservationKey in self.reservations:
            reservation = storage.reservations.get(reservationKey)
            if reservation.accomodationStatus == AccomodationStatus.Canceled:
                continue
            if not dateIntervalsDivergent(start, end, reservation.start, reservation.end):
                return False
        return True

    def addReservation(self, reservationKey):
        self.reservations.append(reservationKey)
```

### Reservation Class
The [Reservation](https://github.com/michal7954/io-project/blob/main/src/classes/Reservation.py) class handles the details of a reservation, including checking room availability and updating reservation statuses.
```python
class Reservation():
    def __init__(self, key, params):
        if correctReservation(params):
            self.key = key
            self.roomKey = int(params[0])
            self.objectStatus = ObjectStatus.Ok

            self.start = Date(params[1])
            self.end = Date(params[2])
            self.accomodationStatus = AccomodationStatus.Reserved
            self.paymentStatus = PaymentStatus.Unpaid
            self.name = str(params[3])
            self.surname = str(params[4])
            self.pesel = str(params[5])
            self.phone = str(params[6])
            self.paymentMethod = PaymentMethod.NotChosen

            room = storage.rooms.get(self.roomKey)
            if not room.checkAvailability(self.start, self.end):
                print('\tRoom not available for this period')
                self.objectStatus = ObjectStatus.Forbidden
            else:
                room.addReservation(self.key)
        else:
            self.objectStatus = ObjectStatus.Forbidden

    def __str__(self):
        return f'#{self.key} room #{self.roomKey}, {self.start}-{self.end}, status {self.accomodationStatus.description}, guest details: {self.name} {self.surname}, PESEL: {self.pesel}, phone: {self.phone}'
```

### Main Function
The [main](https://github.com/michal7954/io-project/blob/main/src/main.py) application entrypoint function initializes the data storage, populates it with sample data, and then starts a listener loop that waits for user input to perform various operations.
```python
def main():
    # data storage initialization
    initStorage()

    # populate storage with sample data
    initData()

    # loop listening for user input operations
    listener()
```

### Operations Enum
The [Operations](https://github.com/michal7954/io-project/blob/main/src/definitions/Operations.py) enum defines all the operations that can be performed by users in the application. Each operation includes an identifier, a description, a list of parameters, and a method or lambda function to be executed.
```python
class Operations(Enum):
    # Definitions of all available operations performed by users in the application

    addRoom = (
        'addRoom',
        'Add Room',
        [Params.roomNumber, Params.roomSize, Params.costPerDay, Params.standard],
        storage.rooms.add
    )
    modifyRoom = (
        'modifyRoom',
        'Modify Room',
        [Params.roomID, Params.roomNumber, Params.roomSize, Params.costPerDay, Params.standard],
        storage.rooms.modify
    )
    removeRoom = (
        'removeRoom',
        'Remove Room',
        [Params.roomID],
        storage.rooms.remove
    )
    # Other operations...
```
