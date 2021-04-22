import math

def obliczenie_pola_i_obwodu_rombu():
    napis_d1 = input('Podaj pierwsza przekatna rombu: ')
    napis_d2 = input('Podaj druga przekatna rombu: ')
    d1 = konwertuj_na_liczbe(napis_d1)
    d2 = konwertuj_na_liczbe(napis_d2)

    if d1 > 0 and d2 > 0:
        wyswietl_wyniki(d1, d2)
    else:
        print(f'Podano nieprawidlowe dane')

def wyswietl_wyniki(d1, d2):
    obwod = obliczyc_obwod_rombu(d1, d2)
    pole = obliczyc_pole_rombu(d1, d2)
    print(f'Obwod rombu wynosi: {obwod}, pole rombu wynosi: {pole}')

def konwertuj_na_liczbe(napis):
    try:
        liczba = float(napis)
        if liczba == 0:
            print(f'Przekatna nie moze byc 0')
            return 0

        return liczba
    except ValueError:
        print(f'Przekatna: {napis} nie jest liczba')
        return 0

def obliczyc_obwod_rombu(d1, d2):
    bok = math.sqrt(((0.5 * d1) ** 2) + ((0.5 * d2) ** 2))
    return 4 * bok

def obliczyc_pole_rombu(d1, d2):
    return (d1 * d2)/2

obliczenie_pola_i_obwodu_rombu()

