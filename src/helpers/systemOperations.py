import storage


def login():
    from definitions.Users import Users

    print()
    print('Wybierz użytkownika')
    print('[identyfikator: opis użytkownika]')
    for user in Users:
        print(user.getMenuOption())

    user = input('Podaj identyfikator: ')

    # użytkownik nie istnieje
    if not hasattr(Users, user):
        print('\tNiepoprawny identyfikator użytkownika')
    else:
        storage.currentUser = user


def logout(_):
    storage.currentUser = None


def listener():
    # funkcja nasłuchująca operacji od użytkownika
    from definitions.Users import Users
    from helpers.getUserOperation import getUserOperation

    while True:

        # logowanie użytkownika
        if storage.currentUser == None:
            login()
            continue

        # pobranie listy dostępnych operacji
        userOperations = Users[storage.currentUser].operations

        # wypisz dostępne operacje
        print()
        print('Wybierz operację')
        print('[#numer identyfikator: opis operacji]')
        for index, operation in enumerate(userOperations, start=1):
            print(f'#{index} {operation.getMenuOption()}')

        operation = input('Podaj numer lub identyfikator: ')
        operation = getUserOperation(operation, userOperations)

        # operacja nie istnieje
        if operation == None:
            print('\tNiepoprawny identyfikator operacji')
            continue

        n = len(operation.params)
        inputParams = [None for _ in range(n)]

        # zebranie niezbędnych parametrów operacji
        for i in range(n):
            param = operation.params[i]
            if type(param) == str:
                # wyświetl tekst pomocniczy
                print(param)
            else:
                # wczytuj parametr dopóki nie ma poprawnego formatu
                while True:
                    inputParams[i] = input(param.text())
                    if param.isCorrect(inputParams[i]):
                        break

        operation.run(inputParams)
