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
        return False

    # Czy są liczbami
    if not date[0].isdigit():
        return False
    if not date[1].isdigit():
        return False
    if not date[2].isdigit():
        return False

    # Czy poprawna długość członów
    if len(date[0]) < 0 or len(date[0]) > 2 or len(date[1]) < 0 or len(date[1]) > 2 or len(date[2]) != 4:
        return False

    # Rok między 2022 a 2030
    if int(date[2]) < 2022 or int(date[2]) > 2030:
        return False

    # Czy poprawnie wprowadzony miesiąc
    if int(date[1]) > 12 or int(date[1]) < 1:
        return False

    # Przypadek roku przestępnego
    if int(date[1]) == 2 and int(date[2]) % 4 == 0 and int(date[0]) < 30 and int(date[0]) > 0:
        return True

    # Czy liczba dni zgadza się z liczbą dni danego miesiąca
    T = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if int(date[0]) < 1 or int(date[0]) > T[int(date[1]) - 1]:
        return False

    return True


# Poprawność wprowadzanego imienia
def correctName(s):
    # Czy dłuższe niż 2
    if len(s) < 2:
        return False

    # Czy składa się z liter
    if s.isalpha() == False:
        return False

    # Czy pierwsza litera jest wielka
    if s[0].isupper() == False:
        return False

    # Czy reszta liter jest mała
    if s[1:].islower() == False:
        return False

    return True


# Poprawność wprowadzanego nazwiska
def correctSurname(s):
    # Rozdzielenie dwuczłonowego nazwiska
    surname = s.split('-')
    if len(surname) != 2 and len(surname) != 1:
        return False

    # Jak w imieniu
    for i in range(len(surname)):
        if len(s) < 2:
            return False

        if s.isalpha() == False:
            return False

        if s[0].isupper() == False:
            return False

        if s[1:].islower() == False:
            return False

    return True


# Poprawność wprowadzanego peselu
def correctPesel(s):
    # Czy poprawna długość i czy składa się z cyfr
    if len(s) != 11:
        return False
    if not s.isdigit():
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
            return False
        for i in range(3):
            if len(phone[i]) != 3 or phone[i].isdigit() == False:
                return False
        return True

    # Wariant 3 - tylko rozdzelenie spacjami
    phone = s.split(' ')
    if len(phone) == 3:
        for i in range(3):
            if len(phone[i]) != 3 or phone[i].isdigit() == False:
                return False
        return True

    if len(phone) == 4:
        for i in range(4):
            if i == 2:
                if len(phone[i]) != 3 or phone[i].isdigit() == False:
                    return False
            else:
                if len(phone[i]) != 2 or phone[i].isdigit() == False:
                    return False
        return True

    return False


# Poprawność wprowadzania numeru pokoju
def correctRoomNumber(s):
    if len(s) > 3 or len(s) == 0 or int(s) <= 0:
        return False
    if s.isdigit():
        return True
    return False


# Poprawność wprowadzania rozmiaru pokoju - 1 lub 2 osobowe
def correctRoomSize(s):
    if not s.isdigit():
        return False
    if int(s) == 1 or int(s) == 2 or int(s) == 3 or int(s) == 4 or int(s) == 5:
        return True
    return False


# Poprawność wprowadzania kosztu - np. 13.00
def correctCostPerDay(s):
    cost = s.split(".")
    if len(cost) != 2 or len(cost[1]) > 2 or not cost[0].isdigit() or not cost[1].isdigit():
        return False
    return True


def correctPaymentMethod(s):
    if s == 'gotówka' or s == 'karta' or s == 'telefon' or s == 'BLIK':
        return True

    return False

def correctStandard(s):
    if len(s)<1 or len(s)>3:
        return False
    for i in range(len(s)):
        if s[i]!='*':
            return False
    return True


def correctRoomID(s):
    if not s.isdigit():
        return False
    for element in storage.rooms.elements.values():
        if (int(element.key) == int(s)):
            return True
    return False


def correctReservationID(s):
    if not s.isdigit():
        return False
    for element in storage.reservations.elements.values():
        if (int(element.key) == int(s)):
            return True
    return False
