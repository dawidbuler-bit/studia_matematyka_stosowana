
import math

a = int(input("Podaj pierwszą liczbę : "))
b = int(input("Podaj drugą liczbę : "))

suma = a + b
roznica = a - b
iloczyn = a * b
iloraz = a / b

sqr_sumy = math.sqrt(a + b)
pot_a = b ** a
pot_b = a ** b

print("Wynik dodawania ", a, "oraz", b, ":", suma, "\n ",
      "Wynik odejmowania ", a, "oraz", b, ":", roznica, "\n",
      "Wynik iloczynu", a, "oraz", b, ":", iloczyn, "\n",
      "Wynik ilorazu ", a, "oraz", b, ":", iloraz, "\n",
      "Wynik pierwiastka kwadratowego sumy ", a, "oraz", b, ":", sqr_sumy, "\n"
      "Wynik liczby", a, "podniesionej do potęgi", b, ":", pot_b, "\n",
      "Wynik liczby", b, "podniesionej do potęgi", a, ":", pot_a)


def okrag(r):
    if r < 0 : return False
    pole = math.pi*(r**2)
    obwod = math.pi*(2*r)
    return "Pole koła o promieniu: ", r, "wynosi: ", pole, "\n" "Obwód koła o promieniu: ", r, "wynosi: ", obwod
print(okrag(13))

n = int(input("Podaj liczbę : "))
ciag_1 = []
for i in range(1,n+1):
    ciag_1.append(i)
print(ciag_1)

ciag_2 = []
for i in range(n,0,-1):
    ciag_2.append(i)
print(ciag_2)

kwadraty = []
for i in range(0,21):
    kwadraty.append(i**2)
print(kwadraty)

szesciany = []
for i in range(10,21):
    szesciany.append(i**3)
print(szesciany)


odwrotnosci = []
for i in range(16,5,-1):
    odwrotnosci.append(i**(-1))
print(odwrotnosci)


a = ['Ala', 'Ela', 'Adam', 'Janek']
for i in range(len(a)):
    print(a[i], len(a[i]))

l1 = ['a', 'b', 'c']
l2 = ['d', 'e']
for x in l1:
    for y in l2:
        print(x, y)
        print(y, x)


a=1
while a<10:
    a=a+1
    print(a)
    if a == 10:
        break
print("koniec")


for i in range(100):
    if i == 50:
        break
print(i)


x=[2,-1,3,-2,9]
for i in x:
    if i<0:
        continue
    print(i**0.5)

for i in range(0,101):
    if i % 6 == 0:
        continue
    print(i**2)


for i in range(1,1001):
    if i % 25 != 0:
        continue
    print(i**2)


def pierw(n):
    if n>=0: return n**0.5
    else: return (-n)**0.5*1j
print(pierw(-16))


def odwrt(a,b):
    if a == 0 or b == 0:
        return False
    return a**(-1) + b**(-1)

print(odwrt(0,1))


def rs(a,b):
    return a+b,a-b

print(rs(2,1))



def suma(*arg):
    s=0
    for x in arg:
        s=s+x
    return s

print(suma(12,13,14))


pierwsza = [1,3,4,5,9,10]
for i in pierwsza:
    if i % 2:
        print(i**2)



n = '123-321-123'
x = n.split('-')
y = ''.join(x)
print(y)


