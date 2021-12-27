from helpers.initStorage import initStorage
from helpers.initData import initData


def main():
    # przygotowanie magazynu danych
    initStorage()

    # wypełnienie magazynu przykładowymi danymi
    initData()

    from definitions.Operations import Operations

    def listener():
        # funkcja nasłuchująca operacji od użytkownika

        while True:

            # wypisz dostępne operacje
            print()
            for operation in Operations:
                operation.menuOption()

            operation = input()

            # operacja nie istnieje
            if not hasattr(Operations, operation):
                print('Niepoprawna nazwa operacji')
                continue

            operation = Operations[operation]

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
    


