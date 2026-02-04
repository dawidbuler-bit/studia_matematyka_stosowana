slownik = {"klucz1": "wartosc1", "klucz2": "wartosc2"}
slownik["klucz3"] = "wartosc3"  # Dodanie nowego elementu
print(slownik)


klucz = "klucz1"
if klucz in slownik:
    print(f"Klucz '{klucz}' istnieje w słowniku.")
else:
    print(f"Klucz '{klucz}' nie istnieje w słowniku.")



slownik1 = {"klucz1": "wartosc1", "klucz2": "wartosc2"}
slownik2 = {"klucz2": "nowa_wartosc", "klucz3": "wartosc3"}

for k, v in slownik2.items():
    if k not in slownik1:
        slownik1[k] = v

print(slownik1)


slownik1 = {"a": 1, "b": 2}
slownik2 = {"c": 3, "d": 4}

polaczony_slownik = {**slownik1, **slownik2}  # Rozpakowanie słowników
print(polaczony_slownik)


produkty = {f"produkt{i}": round(10 + i * 1.1, 2) for i in range(1, 11)}

# Najdroższy i najtańszy produkt
najdrozszy = max(produkty, key=produkty.get)
najtanszy = min(produkty, key=produkty.get)
print(f"Najdroższy produkt: {najdrozszy} - cena: {produkty[najdrozszy]}")
print(f"Najtańszy produkt: {najtanszy} - cena: {produkty[najtanszy]}")

# Suma cen
suma_cen = sum(produkty.values())
print(f"Suma cen: {suma_cen}")

# Średnia cena
srednia_cena = suma_cen / len(produkty)
print(f"Średnia cena: {srednia_cena}")


produkty = {"produkt1": 10.5, "produkt2": 15.3, "produkt3": 20.8}
klucz = input("Podaj nazwę klucza: ")

if klucz in produkty:
    print(f"Klucz '{klucz}' ma wartość: {produkty[klucz]}")
else:
    print("Podany klucz nie istnieje w słowniku.")


liczba = int("12345678901234567890123456789012345678901234567890")
cyfry_w_liczbie = {str(i): str(liczba).count(str(i)) for i in range(10)}
print(cyfry_w_liczbie)



import random

random.seed(42)  # Ustawienie ziarna generatora

a = random.randint(3, 7)
b = random.randint(3, 7)

X = set(random.randint(0, 10) for _ in range(a))
Y = set(random.randint(0, 10) for _ in range(b))

# Informacje o liczbach 5 w X
print("5 należy do zbioru X." if 5 in X else "5 nie należy do zbioru X.")

# Podzbiory
print("X jest podzbiorem Y." if X.issubset(Y) else "X nie jest podzbiorem Y.")
print("Y jest podzbiorem X." if Y.issubset(X) else "Y nie jest podzbiorem X.")

# Operacje na zbiorach
print(f"Suma zbiorów: {X | Y}")
print(f"Różnica X - Y: {X - Y}")
print(f"Różnica Y - X: {Y - X}")
print(f"Iloczyn zbiorów: {X & Y}")
print(f"Różnica symetryczna: {X ^ Y}")

# Najwyższy element
najwyzszy = max(X | Y) if X or Y else None
print(f"Najwyższy element w obu zbiorach: {najwyzszy}")

# Czyszczenie zbiorów
X.clear()
Y.clear()
print(f"X: {X}, Y: {Y}")
