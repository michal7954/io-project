import storage


# Weryfikacja poprawnosci wprowadzanych danych

def correctRoom(params):
    if correctStandard(str(params[3])) and correctRoomNumber(str(params[0])) and correctRoomSize(str(params[1])) and correctCostPerDay(str(params[2])):
        return True
    return False


def correctReservation(params):
    if correctRoomID(str(params[0])) and correctDate((params[1])) and correctDate((params[2])) and correctName(str(params[3])) and correctSurname(str(params[4])) and correctPesel(str(params[5])) and correctPhone(str(params[6])):
        from classes.Date import Date
        start = Date(params[1])
        end = Date(params[2])
        if start < end:
            return True
        else:
            print('\tNiepoprawny okres rezerwacji\n\tWprowadź rezerwację jeszcze raz')

    return False


# Poprawność wprowadzanej daty
def correctDate(s):
    # Data rodzdzielana '.'
    date = s.split('.')

    errorTextPrefix = '\tBłędnie wprowadzona data\n\t'

    # Czy data ma 3 człony
    if len(date) != 3:
        print(f'{errorTextPrefix}Data musi zostać wprowadzona w formacie [dzień.miesiąc.rok]')
        return False

    # Czy są liczbami
    if not date[0].isdigit() or not date[1].isdigit() or not date[2].isdigit():
        print(f'{errorTextPrefix}Dzień, miesiąc i rok muszą być podane jako liczby')
        return False

    # Czy poprawna długość członów
    if len(date[0]) < 0 or len(date[0]) > 2 or len(date[1]) < 0 or len(date[1]) > 2 or len(date[2]) != 4:
        print(f'{errorTextPrefix}Dzień, miesiąc muszą być podane jako liczby jedno lub dwucyfrowe, a rok jako liczba czterocyfrowa')
        return False

    # Rok między 2022 a 2030
    if int(date[2]) < 2022 or int(date[2]) > 2030:
        print(f'{errorTextPrefix}Rok musi być podany z przedziału 2022-2030.')
        return False

    # Czy poprawnie wprowadzony miesiąc
    if int(date[1]) > 12 or int(date[1]) < 1:
        print(f'{errorTextPrefix}Miesiąc musi być z przedziału 1-12.')
        return False

    # Przypadek roku przestępnego
    if int(date[1]) == 2 and int(date[2]) % 4 == 0 and int(date[0]) < 30 and int(date[0]) > 0:
        return True

    # Czy liczba dni zgadza się z liczbą dni danego miesiąca
    T = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if int(date[0]) < 1 or int(date[0]) > T[int(date[1]) - 1]:
        print(f'{errorTextPrefix}Podany dzień jest nieprawidłowy.')
        return False

    return True


# Poprawność wprowadzanego imienia
def correctName(s, paramName='imię'):
    errorTextPrefix = f'\tBłędnie wprowadzone {paramName}\n\t'

    # Czy dłuższe niż 2
    if len(s) < 2:
        print(f'{errorTextPrefix}{paramName} musi zawierać więcej niż 2 litery')
        return False

    # Czy składa się z liter
    if s.isalpha() == False:
        print(f'{errorTextPrefix}{paramName} musi zawiarać wyłącznie litery')
        return False

    # Czy pierwsza litera jest wielka
    if s[0].isupper() == False:
        print(f'{errorTextPrefix}Pierwsza litera musi być wielka')
        return False

    # Czy reszta liter jest mała
    if s[1:].islower() == False:
        print(f'{errorTextPrefix}Tylko pierwsza litera może być wielka.')
        return False

    return True


# Poprawność wprowadzanego nazwiska
def correctSurname(s):
    # Rozdzielenie dwuczłonowego nazwiska
    surname = s.split('-')
    if len(surname) != 2 and len(surname) != 1:
        print('\tBłędnie wprowadzone nazwisko\n\t Nazwisko musi być jednoczłonowe lub dwuczłonowe oddzielone znakim '-'')
        return False

    # Korzysta z imienia
    for i in range(len(surname)):
        if correctName(surname[i], 'nazwisko') == False:
            return False

    return True


# Poprawność wprowadzanego peselu
def correctPesel(s):
    # Czy poprawna długość i czy składa się z cyfr
    if len(s) != 11 or s.isdigit() == False:
        print('\tBłędnie wprowadzony numer PESEL\n\tPESEL musi zawierać 11 cyfr')
        return False

    return True


# Poprawność wprowadzanego numeru telefonu
# Możliwe warianty: 1).123456789, 2).123-456-789, 3).123 456 789, 4).12 34 567 89
def correctPhone(s):
    # Wariant 1 - czy odpowiednia długość i czy składa się z cyfr
    if len(s) == 9 and s.isdigit():
        return True

    errorTextPrefix = '\tBłędnie wprowadzony numer telefonu\n\t'

    # Wariant 2 - tylko rozdzielenie '-'
    phone = s.split('-')
    if len(phone) != 1:
        if len(phone) != 3:
            print(f'{errorTextPrefix}Znak - musi rodzielać po 3 cyfry [123-456-789]')
            return False
        for i in range(3):
            if len(phone[i]) != 3 or phone[i].isdigit() == False:
                print(f'{errorTextPrefix}Znak - musi rodzielać po 3 cyfry [123-456-789]')
                return False
        return True

    # Wariant 3 - tylko rozdzelenie spacjami
    phone = s.split(' ')
    if len(phone) == 3:
        for i in range(3):
            if len(phone[i]) != 3 or phone[i].isdigit() == False:
                print(f'{errorTextPrefix}Znak spacja musi rodzielać cyfry w jeden z podanych sposobów [123 456 789, 12 34 567 89]')
                return False
        return True

    if len(phone) == 4:
        for i in range(4):
            if i == 2:
                if len(phone[i]) != 3 or phone[i].isdigit() == False:
                    print(f'{errorTextPrefix}Znak spacja musi rodzielać cyfry w jeden z podanych sposobów [123 456 789, 12 34 567 89]')
                    return False
            else:
                if len(phone[i]) != 2 or phone[i].isdigit() == False:
                    print(f'{errorTextPrefix}Znak spacja musi rodzielać cyfry w jeden z podanych sposobów [123 456 789, 12 34 567 89]')
                    return False
        return True
    print(f'{errorTextPrefix}Numer musi zostać w wprowadzony w jeden z podanych sposobów [123456789, 123-456-789, 123 456 789, 12 34 567 89]')
    return False


# Poprawność wprowadzania numeru pokoju
def correctRoomNumber(s):
    errorTextPrefix = 'Błędnie wprowadzony numer pokoju\n\t'

    if not s.isdigit():
        print(f'{errorTextPrefix}Numer musi być liczbą')
        return False
    if len(s) > 3 or len(s) == 0 or int(s) <= 0:
        print(f'{errorTextPrefix}Numer musi być liczbą z przedziału 1-999')
        return False
    return True


# Poprawność wprowadzania rozmiaru pokoju - max 5 osobowe
def correctRoomSize(s):
    errorTextPrefix = 'Błędnie wprowadzony rozmiar pokoju\n\t'

    if not s.isdigit():
        print(f'{errorTextPrefix}Rozmiar musi być cyfrą')
        return False
    if int(s) > 0 and int(s) < 6:
        return True
    print(f'{errorTextPrefix}Rozmiar musi być cyfrą z przedziału 1-5')
    return False


# Poprawność wprowadzania kosztu - np. 13.00
def correctCostPerDay(s):
    cost = s.split('.')
    if len(cost) != 2 or len(cost[1]) > 2 or not cost[0].isdigit() or not cost[1].isdigit():
        print('\tBłędnie wprowadzony koszt pokoju\n\tKoszt musi być podany w jeden z podanych sposobów [12.0 lub 12.00]')
        return False
    return True


# Poprawność metod płatności
def correctPaymentMethod(s):
    if s == 'gotówka' or s == 'karta' or s == 'telefon' or s == 'BLIK':
        return True
    print('\tBłędnie wprowadzona metoda płatności\n\tNależy podać jedną z podanych metod [gotówka, karta, telefon, BLIK]')
    return False


def correctStandard(s):
    errorText = '\tBłędnie wprowadzony standard pokoju\n\tDostępne standardy: [*, **, ***]'

    if len(s) < 1 or len(s) > 3:
        print(errorText)
        return False

    for i in range(len(s)):
        if s[i] != '*':
            print(errorText)
            return False
    return True

def correctString(s):
     return True
     

def correctDateHour(s):
    errorText = '\tBłędnie wprowadzony termin usługi\n\tPoprawny format: 1.1.2022 13:30'
    time = s.split(' ')

    if len(time) != 2:
        print(errorText)
        return False

    if not correctDate(time[0]):
        print(errorText)
        return False

    hour = time[1].split(':')

    # Czy są liczbami
    if not hour[0].isdigit() or not hour[1].isdigit():
        print(errorText)
        return False

    # Czy poprawna długość członów
    if len(hour[0]) < 0 or len(hour[0]) > 2 or len(hour[1]) != 2:
        print(errorText)
        return False

    if int(hour[0]) < 0 or int(hour[0]) > 24:
        print(errorText)
        return False

    if int(hour[1]) < 0 or int(hour[1]) > 60:
        print(errorText)
        return False

    return True




def correctRoomID(s):
    errorTextPrefix = '\tBłędnie wprowadzone ID pokoju\n\t'

    if not s.isdigit():
        print(f'{errorTextPrefix}ID pokoju musi być liczbą')
        return False
    if storage.rooms.hasattr(int(s)):
        return True
    print(f'{errorTextPrefix}Brak pokoju o podanym ID w bazie')
    return False


def correctReservationID(s):
    errorTextPrefix = '\tBłędnie wprowadzone ID rezerwacji\n\t'

    if not s.isdigit():
        print(f'{errorTextPrefix}ID rezerwacji musi być liczbą')
        return False
    if storage.reservations.hasattr(int(s)):
        return True
    print(f'{errorTextPrefix}Brak rezerwacji o podanym ID w bazie')
    return False

def correctServiceID(s):
    errorTextPrefix = '\tBłędnie wprowadzone ID usługi\n\t'

    if not s.isdigit():
        print(f'{errorTextPrefix}ID usługi musi być liczbą')
        return False
    if storage.services.hasattr(int(s)):
        return True
    print(f'{errorTextPrefix}Brak usługi o podanym ID w bazie')
    return False
