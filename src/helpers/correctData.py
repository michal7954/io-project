import storage


# Weryfikacja poprawnosci wprowadzanych danych

def correctRoom(params):
    if correctStandard(str(params[3])) and correctRoomNumber(str(params[0])) and correctRoomSize(str(params[1])) and correctCostPerDay(str(params[2])):
        return True
    return False


def correctReservation(params):
    if correctRoomID(str(params[0])) and correctDate((params[1])) and correctDate((params[2])) and correctName(str(params[3])) and correctSurname(str(params[4])) and correctPesel(str(params[5])) and correctPhone(str(params[6])):
        start=params[1].split('.')
        end = params[2].split('.')
        a=int(start[0])+int(start[1])*100+int(start[2])*10000
        b = int(end[0]) + int(end[1]) * 100 + int(end[2]) * 10000
        if b>a:
            return True
    return False


# Poprawność wprowadzanej daty
def correctDate(s):
    # Data rodzdzielana '.'
    date = s.split('.')

    # Czy data ma 3 człony
    if len(date) != 3:
        print("\tBłędnie wprowadzona data\n\tData musi zostać wprowadzona w formacie [[dzień].[miesiąc].[rok]]")
        return False

    # Czy są liczbami
    if not date[0].isdigit() or not date[1].isdigit() or not date[2].isdigit():
        print("\tBłędnie wprowadzona data\n\tDzień, miesiąc i rok muszą byś podane jako liczby")
        return False

    # Czy poprawna długość członów
    if len(date[0]) < 0 or len(date[0]) > 2 or len(date[1]) < 0 or len(date[1]) > 2 or len(date[2]) != 4:
        print("\tBłędnie wprowadzona data\n\tDzień, miesiąc muszą byś podane jako liczby jedno lub dwucyfrowe, a rok jako liczba czterocyfrowa")
        return False

    # Rok między 2022 a 2030
    if int(date[2]) < 2022 or int(date[2]) > 2030:
        print("\tBłędnie wprowadzona data\n\tRok musi byś podany z przedziału 2022-2030.")
        return False

    # Czy poprawnie wprowadzony miesiąc
    if int(date[1]) > 12 or int(date[1]) < 1:
        print("\tBłędnie wprowadzona data\n\tMiesiąc musi byś podane z przedziału 1-12.")
        return False

    # Przypadek roku przestępnego
    if int(date[1]) == 2 and int(date[2]) % 4 == 0 and int(date[0]) < 30 and int(date[0]) > 0:
        return True

    # Czy liczba dni zgadza się z liczbą dni danego miesiąca
    T = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if int(date[0]) < 1 or int(date[0]) > T[int(date[1]) - 1]:
        print("\tBłędnie wprowadzona data\n\tPodany dzień jest nieprawidłowy.")
        return False

    return True




# Poprawność wprowadzanego imienia
def correctName(s, name="imię"):
    # Czy dłuższe niż 2
    if len(s) < 2:
        print(f"\tBłędnie wprowadzone {name}\n\t{name} musi zawierać więcej niż 2 litery")
        return False

    # Czy składa się z liter
    if s.isalpha() == False:
        print("f\tBłędnie wprowadzone {name}\n\t{name} musi zawiarać wyłącznie litery")
        return False

    # Czy pierwsza litera jest wielka
    if s[0].isupper() == False:
        print(f"\tBłędnie wprowadzone {name}\n\tPierwsza litera musi być wielka")
        return False

    # Czy reszta liter jest mała
    if s[1:].islower() == False:
        print(f"\tBłędnie wprowadzone {name}\n\tTylko pierwsza litera może być wielka.")
        return False

    return True



# Poprawność wprowadzanego nazwiska
def correctSurname(s):
    # Rozdzielenie dwuczłonowego nazwiska
    surname = s.split('-')
    if len(surname) != 2 and len(surname) != 1:
        print("\tBłędnie wprowadzone nazwisko\n\t Nazwisko musi byś jednoczłonowe lub dwuczłonowe oddzielone znakim '-'")
        return False

    # Korzysta z imienia
    for i in range(len(surname)):
        if correctName(surname[i],"nazwisko") == False:
            return False

    return True



# Poprawność wprowadzanego peselu
def correctPesel(s):
    # Czy poprawna długość i czy składa się z cyfr
    if len(s) != 11 or s.isdigit() == False:
        print("\tBłędnie wprowadzony numer PESEL\n\t PESEL musi zawierać 11 cyfr")
        return False

    return True



# Poprawność wprowadzanego numeru telefonu
# Możliwe warianty: 1).123456789, 2).123-456-789, 3).123 456 789, 4).12 34 567 89
def correctPhone(s):
    # Wariant 1 - czy odpowiednia długość i czy składa się z cyfr
    if len(s) == 9 and s.isdigit():
        return True

    # Wariant 2 - tylko rozdzielenie '-'
    phone = s.split('-')
    if len(phone) != 1:
        if len(phone) != 3:
            print("\tBłędnie wprowadzony numer telefonu\n\tZnak '-' musi rodzielać po 3 cyfry [123-456-789]")
            return False
        for i in range(3):
            if len(phone[i]) != 3 or phone[i].isdigit() == False:
                print("\tBłędnie wprowadzony numer telefonu\n\tZnak '-' musi rodzielać po 3 cyfry [123-456-789]")
                return False
        return True

    # Wariant 3 - tylko rozdzelenie spacjami
    phone = s.split(' ')
    if len(phone) == 3:
        for i in range(3):
            if len(phone[i]) != 3 or phone[i].isdigit() == False:
                print("\tBłędnie wprowadzony numer telefonu\n\tZnak 'spacja' musi rodzielać cyfry w jeden z podanych sposobów [123 456 789] lub [12 34 567 89]")
                return False
        return True

    if len(phone) == 4:
        for i in range(4):
            if i == 2:
                if len(phone[i]) != 3 or phone[i].isdigit() == False:
                    print("\tBłędnie wprowadzony numer telefonu\n\tZnak 'spacja' musi rodzielać cyfry w jeden z podanych sposobów [123 456 789] lub [12 34 567 89]")
                    return False
            else:
                if len(phone[i]) != 2 or phone[i].isdigit() == False:
                    print("\tBłędnie wprowadzony numer telefonu\n\tZnak 'spacja' musi rodzielać cyfry w jeden z podanych sposobów [123 456 789] lub [12 34 567 89]")
                    return False
        return True
    print("\tBłędnie wprowadzony numer telefonu\n\tNumer musi zostać w wprowadzony w jeden z podanych sposobów [123456789] lub [123-456-789] lub [123 456 789] lub [12 34 567 89]")
    return False



# Poprawność wprowadzania numeru pokoju
def correctRoomNumber(s):
    if not s.isdigit():
        print("Błędnie wprowadzony numer pokoju\n\tNumer musi być liczbą")
        return False
    if len(s) > 3 or len(s) == 0 or int(s) <= 0:
        print("Błędnie wprowadzony numer pokoju\n\tNumer musi być liczbą z przedziału 1-999")
        return False
    return True



# Poprawność wprowadzania rozmiaru pokoju - max 5 osobowe
def correctRoomSize(s):
    if not s.isdigit():
        print("Błędnie wprowadzony rozmiar pokoju\n\tRozmiar musi być cyfrą")
        return False
    if int(s) > 0 and int(s) < 6:
        return True
    print("\tBłędnie wprowadzony rozmiar pokoju\n\tRozmiar musi być cyfrą z przedziału 1-5.")
    return False



# Poprawność wprowadzania kosztu - np. 13.00
def correctCostPerDay(s):
    cost = s.split(".")
    if len(cost) != 2 or len(cost[1]) > 2 or not cost[0].isdigit() or not cost[1].isdigit():
        print("\tBłędnie wprowadzony koszt pokoju\n\tKoszt musi być podany w jeden z podanych sposobów [12.0 lub 12.00]")
        return False
    return True


# Poprawność metod płatności
def correctPaymentMethod(s):
    if s == 'gotówka' or s == 'karta' or s == 'telefon' or s == 'BLIK':
        return True
    print("\tBłędnie wprowadzona metoda płatności\n\tNależy podać jedną z podanych metod ['gotówka','karta','telefon','BLIK']")
    return False


def correctStandard(s):
    if len(s) < 1 or len(s) > 3:
        print("\tBłędnie wprowadzony standard pokoju\n\tDostępne standardy: [*, **, ***]")
        return False

    for i in range(len(s)):
        if s[i] != '*':
            print("\tBłędnie wprowadzony standard pokoju\n\tDostępne standardy: [*, **, ***]")
            return False
    return True



def correctRoomID(s):
    if not s.isdigit():
        print("\tBłędnie wprowadzone ID pokoju\n\tID pokoju musi byś liczbą")
        return False
    for element in storage.rooms.elements.values():
        if (int(element.key) == int(s)):
            return True
    print("\tBłędnie wprowadzone ID pokoju\n\tBrak pokoju o podanym ID w bazie")
    return False


def correctReservationID(s):
    if not s.isdigit():
        print("\tBłędnie wprowadzone ID rezerwacji\n\tID rezerwacji musi byś liczbą")
        return False
    for element in storage.reservations.elements.values():
        if (int(element.key) == int(s)):
            return True
    print("\tBłednie wprowadzone ID rezerwacji.\n\tBrak rezerwacji o podanym ID w bazie")
    return False

