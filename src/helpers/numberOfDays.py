# Funkcja oblicza ile dni trwa rezerwacja (np. od 28.12 do 31.12 rezerwacja trwa 3 dni - według doby hotelowej)
# Uwezględniane są rózne miesiące rozpoczęcia i zakończenia rezerwacji oraz przypadek roku przestępnego

def numberOfDays(d1,d2):
    T=[31,28,31,30,31,30,31,31,30,31,30,31]

    start=[d1.day,d1.month,d1.year]
    end=[d2.day,d2.month,d2.year]

    if start[1:]==end[1:]:
        return end[0]-start[0]

    counter=0
    if start[1]!=2 or start[2]%4!=0:
        counter+=T[start[1]-1]-start[0]
    else:
        counter+=29-start[0]

    counter+=end[0]

    if start[1]!=12:
        start[1]+=1
    else:
        start[1]=1
        start[2]+=1

    while start[1:]!=end[1:]:
        if start[1] != 2 or start[2] % 4 != 0:
            counter += T[start[1]-1]
        else:
            counter += 29

        if start[1] != 12:
            start[1] += 1
        else:
            start[1] = 1
            start[2] += 1

    return counter




