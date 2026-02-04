import math

krotka = (-1, 2, 3, 4, 5, 6, 7, 8, -2, 10)

suma = 0
for i in krotka:
    suma += i

iloczyn = 1
for i in krotka:
    if i < 6:
        iloczyn *= i

for i in krotka:
    if i < 6:
        print(i)

suma_nieparz = 0
for i in krotka:
    if i % 2 != 0:
        suma_nieparz += i

k = 0
for i in krotka:
    if i % 2 != 0:
        k += 1
print(k)

if 2 in krotka: print("Cyfra 2 jest w krotce")

k = 0
for i in krotka:
    if i > 0:
        k += 1
if k == len(krotka):
    print("Wszstkie wartości są dodatnie")
else:
    print("Nie wszystkie wartości są dodatnie")

a = int(input("podaj element: "))
if a in krotka:
    print("Podany element znajduje się w krotce")
else:
    print("Podany element nie znajduje się w krotce")


def fun1(T, m):
    for i in range(m):
        print(T[i])


fun1([[2, 3, 4, 5], [7, 6, 5, 4], [8, 9, 4, 5]], 3)


def fun2(T, m, n):
    s = 0
    for i in range(m):
        for j in range(n):
            if T[i][j] % 3:
                s += T[i][j]
    return s


print("suma = ", fun2([[2, 3, 4, 5], [7, 6, 5, 4], [8, 9, 4, 5]], 3, 4))


def fun3(T, m, n):
    for i in range(m):
        for j in range(n):
            if i != j:
                T[i][j] -= 3
        print(T[i])


fun3([[2, 3, 4, 5], [7, 6, 5, 4], [8, 9, 4, 5]], 3, 4)

n = int(input("podaj liczbę pierwszych wyrazow rozwiniecia szerega mclaurina: "))
x = int(input("Podaj wykładnik potęgi x: "))
suma = 0
for i in range(0, n + 1):
    suma += ((x ** i) / math.factorial(i))
print(suma)
print(math.exp(3))


def silnia_i(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


print(silnia_i(6))


def silnia_reku(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia_reku(n - 1)


print(silnia_reku(6))


def stirling(n):
    return ((n / math.e) ** n) * math.sqrt(2 * math.pi * n)


print(stirling(52))
print(math.factorial(52))


def fibo_i(n):
    x_0 = 0
    x_1 = 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    for i in range(2, n + 1):
        x_0, x_1 = x_1, x_0 + x_1
    return x_1


def fibo_reku(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_reku(n - 1) + fibo_reku(n - 2)


print(fibo_i(10), fibo_reku(10))


def czy_liczba_doskonala(n):
    if n < 2:
        return False
    suma_dzielników = 0
    for i in range(1, n):
        if n % i == 0:
            suma_dzielników += i
    return suma_dzielników == n


print(czy_liczba_doskonala(496))


def czy_liczba_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print(czy_liczba_pierwsza(127))
