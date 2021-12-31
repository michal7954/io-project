from helpers.getUserOperation import getUserOperation
from helpers.initStorage import initStorage
from helpers.initData import initData
import storage

def main():
    # przygotowanie magazynu danych
    initStorage()

    # wypełnienie magazynu przykładowymi danymi
    initData()

    from definitions.Users import Users
    def login():

        print()
        print('Wybierz użytkownika')
        print('[identyfikator: opis użytkownika]')
        for user in Users:
            user.printMenuOption()

        user = input('Podaj identyfikator: ')

        # użytkownik nie istnieje
        if not hasattr(Users, user):
            print('Niepoprawny identyfikator użytkownika')
        else:
            storage.currentUser = user


    # from definitions.Operations import Operations

    def listener():
        # funkcja nasłuchująca operacji od użytkownika

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
            print('[identyfikator: opis operacji]')
            for operation in userOperations:
                operation.printMenuOption()

            operation = input('Podaj identyfikator: ')
            operation = getUserOperation(operation, userOperations)

            # operacja nie istnieje
            if operation == None:
                print('Niepoprawny identyfikator operacji')
                continue

            n = len(operation.params)
            params = [None for _ in range(n)]

            # zebranie niezbędnych parametrów operacji
            for i in range(n):
                param = operation.params[i]
                if str(param)[0]=='p':
                    print(param[2:])
                else:
                    params[i] = input(param.text())

            operation.run(params)

            # todo zaawansowana weryfikacja i obsługa błędów
            # try:
            #     operation.run(params)
            # except Exception as e:
            #     print('Wystąpił problem')
            #     print(e)

    listener()


if __name__ == '__main__':
    main()
