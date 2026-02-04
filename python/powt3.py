def czy_liczba_pierwsza(n):
    if n < 2 :
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def pierwsza_mersena(n):
    return czy_liczba_pierwsza(2**n -1)


def mersena(n):
    if czy_liczba_pierwsza(n):
        return pierwsza_mersena(2**n -1)
    return False


def czy_liczba_mersennea(m):
    if m < 1: return False
    i = 1
    while 2**i - 1 <= m:
        if 2**i - 1 == m:
            return True
        i += 1
    return False

def czy_liczba_doskonala(n):
    if n < 2:
        return False
    suma_dzielników = 0
    for i in range(1,n):
        if n % i == 0:
            suma_dzielników += i
    return suma_dzielników == n

def znajdz_liczbe_doskonala(n):
    if czy_liczba_pierwsza(n):
        liczba_merssenea = 2**n - 1
        if czy_liczba_pierwsza(liczba_merssenea):
            return liczba_merssenea * 2**(n-1)
    return None


def znajdz_liczbe_doskonala2(n):
    if pierwsza_mersena(n):
            return (2**n - 1) * 2**(n-1)
    return None


def euklides(n):
    if n < 2: return False
    suma = 0
    i = 0
    while not czy_liczba_pierwsza(suma):
        suma = suma + 2**i
        i += 1
    print(suma, i)
    return czy_liczba_doskonala(suma * 2**(i-1))


def euklides2(n):
    if n < 2: return False
    i = 2
    while (2**i - 1)*(2**(i-1)) <= n:
        if pierwsza_mersena(i):
            return (2 ** i - 1) * (2 ** (i - 1)) == n
        i += 1
    return False



def super_pierwsza(n):
    if czy_liczba_pierwsza(n):
        k = sum(int(i) for i in str(n))
        if czy_liczba_pierwsza(k):
            return True
    return False

print(super_pierwsza(37))

dwucyfrowe_super_pierwsze = [n for n in range(10,100) if super_pierwsza(n)]

print(dwucyfrowe_super_pierwsze)


def super_B_pierwsza(n):
    if super_pierwsza(n):
        zapis_binarny = bin(n)[2:]
        suma_cyfr_binarnych = sum(int(i) for i in zapis_binarny)
        if czy_liczba_pierwsza(suma_cyfr_binarnych):
            return True
    return False

dwucyfrowe_super_B_pierwsze = [n for n in range(10, 100) if super_B_pierwsza(n)]

suma_liczb = sum(dwucyfrowe_super_B_pierwsze)

print(dwucyfrowe_super_B_pierwsze, czy_liczba_pierwsza(suma_liczb))