

ciag_znakow = input(str("Podaj jakiś ciąg znaków: "))

if len(ciag_znakow) < 2:
    print([])
else:
    print(ciag_znakow[:2], ciag_znakow[-2:])


#zadanie 3
ciag_znakow = input(str("Podaj jakiś ciąg znaków: "))

print(ciag_znakow.replace(" ",""))

lista = ciag_znakow.split()
print("".join(lista))

#zadanie 4
print(len(ciag_znakow.split()))


#zadanie 5
dane = input(str("Jak się nazywasz? "))
imie = dane.split()[0]
nazwisko = dane.split()[1]
print(imie.replace(imie[:2], nazwisko[-2:]), nazwisko.replace(nazwisko[-2:],imie[:2]))

#zadanie 6
zdanie = input(str("Podaj jakieś zdanie: "))
zdanie = zdanie.replace("tak", "temp")
zdanie = zdanie.replace("nie", "tak")
zdanie = zdanie.replace("temp", "nie")

print(zdanie)

zdanie = zdanie.replace("tak", "temp").replace("nie", "tak").replace("temp", "nie")

print(zdanie)


#zadanie 7

ciag_znakow = input(str("Podaj jakiś ciąg znaków: "))
slownik = {}
for i in ciag_znakow:
    slownik.setdefault(i, 0)
    slownik[i] += 1
print(slownik)

for key, value in slownik.items():
    print("Znak: {0} {1} razy".format(key, value))

print([i for i in ciag_znakow if i != "p"])

#zad 8

def sortuj_litery():
    zdanie = input("Wprowadź zdanie: ")

    litery = ""


    for slowo in zdanie:
        if (slowo.lower() >= 'a' and slowo.lower() <= 'z'):
            litery += slowo.lower()

    posortowane_litery = ""
    while len(litery) > 0:
        najmniejsza = min(litery)
        posortowane_litery += najmniejsza
        litery = litery.replace(najmniejsza, '', 1)

    return print("Litery w kolejności alfabetycznej:", posortowane_litery)



print(sortuj_litery())
