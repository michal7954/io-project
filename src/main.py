from classes.Store import Store
from classes.Room import Room


def main():
    
    storage = {
        "rooms": Store(Room),
        "reservations": Store(Room),
        "services": Store(Room),
        "guests": Store(Room),
    }

    def listener():
        nonlocal storage

        while True:
            line = input()
            params = line.split()

            if len(params)==0:
                continue
            
            store = storage.get(params[0])

            store.call(params)
            
            # try:
            #     store.call(params)
            # except:
            #     print("Problem occurred")

    listener()

main()