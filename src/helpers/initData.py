import storage


def initData():

    storage.rooms.add([1, 4, 40.50, '*'])  # 1
    storage.rooms.add([2, 2, 50.40, '**'])  # 2
    storage.rooms.add([3, 5, 60.55, '***'])  # 3
    storage.rooms.add([4, 4, 40.60, '*'])  # 4
    storage.rooms.add([5, 4, 50.00, '**'])  # 5
    storage.rooms.add([6, 2, 60.15, '***'])  # 6
    storage.rooms.add([7, 2, 40.90, '*'])  # 7
    storage.rooms.add([8, 2, 50.80, '*'])  # 8
    storage.rooms.add([9, 2, 60.00, '***'])  # 9
    storage.rooms.add([10, 4, 40.00, '**'])  # 10
    storage.rooms.add([11, 4, 50.80, '**'])  # 11
    storage.rooms.add([12, 3, 60.25, '***'])  # 12

    storage.rooms.add([14, 3, 40.60, '*'])  # 13
    storage.rooms.add([15, 1, 50.55, '**'])  # 14
    storage.rooms.add([16, 2, 60.90, '***'])  # 15
    storage.rooms.add([17, 3, 40.85, '*'])  # 16
    storage.rooms.add([18, 2, 50.90, '**'])  # 17
    storage.rooms.add([19, 1, 60.00, '***'])  # 18
    storage.rooms.add([20, 1, 49.99, '**'])  # 19

    storage.reservations.add([1, '1.1.2022', '2.1.2022', 'Michał', 'Nowak', '12345678910', '347218904'])  # 1
    storage.reservations.add([1, '3.1.2022', '7.1.2022', 'Joanna', 'Kowalska', '92071314764', '125734890'])  # 2
    storage.reservations.add([1, '7.1.2022', '9.1.2022', 'Klaudia', 'Wiśniewska', '81100216347', '189450893'])  # 3
    storage.reservations.add([1, '10.1.2022', '23.1.2022', 'Natalia', 'Wójcik', '80072909146', '674409125'])  # 4
    storage.reservations.add([1, '9.1.2022', '10.1.2022', 'Oliwia', 'Kowalczyk', '90080517425', '757980865'])  # 5
    storage.reservations.add([1, '24.1.2022', '31.1.2022', 'Kamila', 'Kamińska', '90060804706', '740229678'])  # 6

    storage.reservations.add([6, '1.1.2022', '3.1.2022', 'Damian', 'Lewandowski', '91810112311', '478892220'])  # 7
    storage.reservations.add([6, '3.1.2022', '7.1.2022', 'Grzegorz', 'Zieliński', '66420212332', '690449648'])  # 8
    storage.reservations.add([6, '9.1.2022', '24.1.2022', 'Ewelina', 'Szymańska', '78242967240', '534715896' ])  # 9
    storage.reservations.add([6, '7.1.2022', '9.1.2022', 'Aneta', 'Dąbrowska', '01232907945', '794707034'])  # 10
    storage.reservations.add([6, '24.1.2022', '30.1.2022','Stanisław', 'Woźniak', '99372056795', '663203821'])  # 11

    storage.reservations.add([7, '1.1.2022', '31.1.2022', 'Dominik', 'Kozłowski', '87081472058', '294467200'])  # 12

    storage.reservations.add([14, '1.1.2022', '3.1.2022', 'Kamil', 'Jankowski', '00123027871', '267893621'])  # 13
    storage.reservations.add([14, '10.1.2022', '17.1.2022', 'Paulina', 'Mazur', '92112671146', '378840255'])  # 14
    storage.reservations.add([14, '24.1.2022', '31.1.2022', 'Jan', 'Kwiatkowski', '88100752214', '561129334'])  # 15
