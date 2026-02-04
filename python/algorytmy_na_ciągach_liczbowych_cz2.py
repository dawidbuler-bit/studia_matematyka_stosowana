#zad 1
def szukaj(T):
    licznik = {}

    for element in T:
        licznik.setdefault(element, 0)
        licznik[element] += 1

    max_licznik = max(licznik.values())
    min_licznik = min(licznik.values())

    najczesciej = []
    najrzadziej = []

    for klucz, wartosc in licznik.items():
        if max_licznik == wartosc:
            najczesciej.append(klucz)
        if min_licznik == wartosc:
            najrzadziej.append(klucz)


    return najczesciej, najrzadziej

print(szukaj([4, 4, 2, 2, 2, 3, 1, 1, 6, 6, 0]))




#zad 2
def szukaj_inaczej(T):
    licznik = {}

    for element in T:
        licznik.setdefault(element, 0)
        licznik[element] += 1

    max_licznik = max(licznik.values())
    min_licznik = min(licznik.values())

    najczesciej = []

    if max_licznik > len(T)/2:
        for klucz, wartosc in licznik.items():
            if max_licznik == wartosc:
                return klucz
    return None

print(szukaj_inaczej([4, 4, 4, 4, 4, 4, 4, 1, 6, 6, 0]))



#nie wiem co to
def lid(T):

    n = len(T)
    lider = T[0]
    pom = 1

    for i in range(1,n):
        if pom == 0:
            lider = T[i]
            pom = 1
        elif lider == T[i]:
            pom += 1
        else:
            pom -= 1
    if pom == 0:
        return False
    else:
        ilosc = 0
        for i in range(n):
            if lider == T[i]:
                ilosc += 1
        if ilosc > len(T)/2:
            return lider
        return False

print(lid([4, 4, 4, 6, 6, 6, 6, 1, 6, 6, 0]))


#zad 3?

T = [3, 8, 11, 23, 24, 36, 41, 44, 49, 52]
n = len(T) - 1

def szukaj_lewy_prawy(T, lewy, prawy, element):

    while lewy <= prawy:
            srodek = (lewy+prawy)//2
            if T[srodek] == element:
                return srodek
            elif T[srodek] < element:
                lewy = srodek + 1
            else:
                prawy = srodek - 1

    return -1

print(szukaj_lewy_prawy(T, 0, n, 44))


#zad 4

T = [48, 3, 18, 77, 31]

hash = [i % 11 for i in T]

lista_hash = {}

for i in T:
    lista_hash[i % 11] = i

element = 48

print(element == lista_hash.get(element % 11), lista_hash)



#zad 5
T = [48, 3, 18, 77, 31, 44]

slownik_hash = {}


for i in T:
    slownik_hash.setdefault(i % 11, [])
    slownik_hash[i % 11].append(i)


print(slownik_hash)

element = 77
print(element in slownik_hash.get(element % 11, []))


#zad 6
T = [48, 3, 18, 77, 31, 44]
def tablica_asocjacyjna(T, element):
    rozmiar = len(T) * 2

    slownik_hash = {i: None for i in range(rozmiar)}

    for i in T:
        indeks = i % rozmiar
        while slownik_hash[indeks] is not None:
            indeks = (indeks + 1) % rozmiar
        slownik_hash[indeks] = i
    return slownik_hash


def sprawdz_obecnosc(slownik_hash, element):
    rozmiar = len(slownik_hash)
    indeks = element % rozmiar

    while slownik_hash.get(indeks) is not None:
        if slownik_hash[indeks] == element:
            return True
        indeks = (indeks + 1) % rozmiar
    return False


print(tablica_asocjacyjna(T, 48),sprawdz_obecnosc(tablica_asocjacyjna(T,48),48))


#tworzenie tablicy asocjacyjnej z metoda obslugi kolizji otwartą
def haszuj(T, p):

    slownik_hash = {}

    for i in T:
        slownik_hash.setdefault(i % p, [])
        slownik_hash[i % p].append(i)
    return slownik_hash


#sprawdzanie czy zadany element znajduje sie w tablicy asocjacyjenj
def szukaj_w_tablicy(T, element, p):
    hash = haszuj(T, p)
    return element in hash.get(element % p, [])



print(szukaj(T = [48, 3, 18, 77, 31, 44], element= 77, p = 11), haszuj(T = [48, 3, 18, 77, 31, 44],p = 11))
'''
