# proof of concept
# test pomysłu na obiektowe rozwiązanie w pythonie

rooms = []

class Room:
    def __init__(self, number, size):
        self.id = 'generateId()'
        self.number = number
        self.size = size

def create(params):
    global rooms
    rooms.append(Room(params[1], params[2]))

def get():
    for room in rooms:
        print(room.number, room.size)

def listener():
    while True:
        line = input()
        params = line.split()

        if len(params)==0:
            continue
        
        operator = params[0]
        if operator == 'create':
            create(params)
        elif operator == 'get':
            get()
        else:
            None


listener()

test = """ 
create 1 2
create 2 4
create 3 4
get
"""