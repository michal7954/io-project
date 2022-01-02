import storage
from helpers.correctData import *
from classes.Date import Date


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
        print('Niepoprawny identyfikator użytkownika')
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
            print('Niepoprawny identyfikator operacji')
            continue

        n = len(operation.params)
        params = [None for _ in range(n)]

        # zebranie niezbędnych parametrów operacji
        for i in range(n):
            param = operation.params[i]
            if type(param) == str:
                print(param)
            else:
                while True:
                        params[i] = input(param.text())

                        # Obsługa błędów
                        match = str(param)[7:]

                        if match == 'reservationStart':
                            if correctDate(params[i]) == False:
                                print('Błędnie wprowadzona data')
                            else:
                                break

                        if match == 'reservationEnd':
                            if correctDate(params[i]) == False:
                                print('Błędnie wprowadzona data')
                            else:
                                a=(Date(params[i-1]))
                                b=(Date(params[i]))
                                if not a.__lt__(b):
                                    print('Błędny przedział czasowy')
                                else:
                                    break

                        elif match == 'name':
                            if correctName(params[i]) == False:
                                print('Błędnie wprowadzone imię')
                            else:
                                break

                        elif match == 'surname':
                            if correctSurname(params[i]) == False:
                                print('Błędnie wprowadzone nazwisko')
                            else:
                                break

                        elif match == 'pesel':
                            if correctPesel(params[i]) == False:
                                print('Błędnie wprowadzony numer PESEL')
                            else:
                                break

                        elif match == 'phone':
                            if correctPhone(params[i]) == False:
                                print('Błędnie wprowadzony numer telefonu')
                            else:
                                break

                        elif match == "roomNumber":
                            if correctRoomNumber(params[i]) == False:
                                print('Błędny numer pokoju')
                            else:
                                break

                        elif match == "roomSize":
                            if correctRoomSize(params[i]) == False:
                                print('Błędny rozmiar pokoju')
                            else:
                                break

                        elif match == "costPerDay":
                            if correctCostPerDay(params[i]) == False:
                                print('Błędnie wprowadzony koszt pobytu')
                            else:
                                break

                        elif match == "roomID":
                            if correctRoomID(params[i]) == False:
                                print('Błędne ID')
                            else:
                                break

                        elif match == "reservationID":
                            if correctReservationID(params[i]) == False:
                                print('Błędne ID')
                            else:
                                break
                        elif match == "paymentMethods":
                            if correctPaymentMethod(params[i]) == False:
                                print('Niepoprawna metoda płatności')
                            else:
                                break

                        elif match =="standard":
                            if correctStandard(params[i])==False:
                                print('Niepoprawny standard')
                            else:
                                break
                        
                        else: break
        operation.run(params)
