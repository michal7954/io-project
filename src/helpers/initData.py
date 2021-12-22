import storage


def initData():

    storage.rooms.add([1, 4, 40])  # 1
    storage.rooms.add([2, 2, 50])  # 2
    storage.rooms.add([3, 5, 60])  # 3
    storage.rooms.add([4, 4, 40])  # 4
    storage.rooms.add([5, 4, 50])  # 5
    storage.rooms.add([6, 2, 60])  # 6
    storage.rooms.add([7, 2, 40])  # 7
    storage.rooms.add([8, 2, 50])  # 8
    storage.rooms.add([9, 2, 60])  # 9
    storage.rooms.add([10, 4, 40])  # 10
    storage.rooms.add([11, 4, 50])  # 11
    storage.rooms.add([12, 3, 60])  # 12

    storage.rooms.add([14, 3, 40])  # 13
    storage.rooms.add([15, 1, 50])  # 14
    storage.rooms.add([16, 2, 60])  # 15
    storage.rooms.add([17, 3, 40])  # 16
    storage.rooms.add([18, 2, 50])  # 17
    storage.rooms.add([19, 1, 60])  # 18
    storage.rooms.add([20, 1, 49.99])  # 19

    storage.reservations.add([1, '1.1.2022', '2.1.2022'])  # 1
    storage.reservations.add([1, '3.1.2022', '7.1.2022'])  # 2
    storage.reservations.add([1, '7.1.2022', '9.1.2022'])  # 3
    storage.reservations.add([1, '10.1.2022', '23.1.2022'])  # 4
    storage.reservations.add([1, '9.1.2022', '10.1.2022'])  # 5
    storage.reservations.add([1, '24.1.2022', '31.1.2022'])  # 6

    storage.reservations.add([6, '1.1.2022', '3.1.2022'])  # 7
    storage.reservations.add([6, '3.1.2022', '7.1.2022'])  # 8
    storage.reservations.add([6, '9.1.2022', '24.1.2022'])  # 9
    storage.reservations.add([6, '7.1.2022', '9.1.2022'])  # 10
    storage.reservations.add([6, '24.1.2022', '30.1.2022'])  # 11

    storage.reservations.add([7, '1.1.2022', '31.1.2022'])  # 12

    storage.reservations.add([14, '1.1.2022', '3.1.2022'])  # 13
    storage.reservations.add([14, '10.1.2022', '17.1.2022'])  # 14
    storage.reservations.add([14, '24.1.2022', '31.1.2022'])  # 15
