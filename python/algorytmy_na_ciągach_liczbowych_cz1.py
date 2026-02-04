import random

random.seed(2)

for i in range(5):
    lista = []
    for j in range(10):
        lista.append(random.randint(0, 99))
    print(lista)


lista = []
for i in range(1000):
    lista.append(round((100*random.random()),1))
print(lista)

m = round((100* random.random()),1)

def szukaj(lista,m):
    powt = 0
    for liczba in lista:
        powt += 1
        if m == liczba:
            return True, powt
    return False, powt

print(szukaj(lista,m))


liczba_porownan = []
for _ in range(1000):
    m = round(random.uniform(0, 100), 1)  # Losowa liczba m
    _, porownania = szukaj(lista, m)
    liczba_porownan.append(porownania)

# Obliczanie stosunku średniej liczby porównań do ilości elementów w ciągu
srednia_porownan = sum(liczba_porownan) / len(liczba_porownan)
stosunek = srednia_porownan / len(lista)

print(f"Średnia liczba porównań: {srednia_porownan}")
print(f"Stosunek średniej liczby porównań do ilości elementów w ciągu: {stosunek}")


def ile_razy_wystepuje(ciag, m):
    porownania = 0
    liczba_wystapien = 0
    for liczba in ciag:
        porownania += 1
        if liczba == m:
            liczba_wystapien += 1
    return liczba_wystapien, porownania


import time

# Generowanie większego ciągu (1 000 000 elementów)
duza_lista = [round(random.uniform(0, 100), 1) for _ in range(1_000_000)]
duza_krotka = tuple(duza_lista)

# Pomiar czasu dla listy
start_list = time.time()
szukaj(duza_lista, 50.5)
czas_list = time.time() - start_list

# Pomiar czasu dla krotki
start_tuple = time.time()
szukaj(duza_krotka, 50.5)
czas_tuple = time.time() - start_tuple

print(f"Czas dla listy: {czas_list:.5f} s")
print(f"Czas dla krotki: {czas_tuple:.5f} s")


def znajdz_minimum(ciag):
    porownania = 0
    minimum = ciag[0]
    for liczba in ciag[1:]:
        porownania += 1
        if liczba < minimum:
            minimum = liczba
    return minimum, porownania

# Przykład użycia
najmniejszy, liczba_porownan = znajdz_minimum(lista)
print(f"Najmniejszy element: {najmniejszy}, liczba porównań: {liczba_porownan}")
