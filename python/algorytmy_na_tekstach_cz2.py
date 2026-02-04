def zgodnosc(n, m):
    if len(n) != len(m):
        raise ValueError("Podane wyrażenia nie były tej samej długości")
    zgodne = [el1 for el1, el2 in zip(n, m) if el1 == el2]
    return zgodne , len(zgodne), len(n)-len(zgodne)/len(n * 100)

print(zgodnosc([1,2,3,4,5],[2,1,4,3,5]))


def alfasort(n):
    return sorted(n)

print(alfasort(["101", "10", "11"]))

def sprawdz(n, m):
    slownik = {}
    if len(n) != len(m):
        return False
    def zlicz(n):
        for element in n:
            slownik[element] = slownik.get(element, 0) + 1
        return slownik
    return zlicz(n) == zlicz(m)

print(sprawdz([1,2,3,4,5],[2,1,4,3,5]))

def szukanie(slowo, wzorzec):
    for i in range(len(slowo)-1):
        T = []
        if len(wzorzec) > len(slowo):
            return False
        for i in range(len(slowo) - len(wzorzec) + 1):
            for j in range(i, i + len(wzorzec)):
                if slowo[j] != wzorzec[j - i]:
                    break
            if j + 1 == i + len(wzorzec):
                T.append(i)
        if T == []:
            return False
        return len(T)

print(szukanie("karykatura", "ka"))

def znajdz_wzorzec(slowo, wzorzec):
    licznik = 0
    for i in range(len(slowo) - len(wzorzec) + 1):
        if slowo[i:i+len(wzorzec)] == wzorzec:
            licznik += 1
    return licznik

print(znajdz_wzorzec("karykatura", "ka"))

slowo = "karykatura"
wzorzec = "ka"

def szukanie2(slowo, wzorzec):
    if len(wzorzec) > len(slowo):
        return False
    indeks = slowo.find(wzorzec)
    licznik = 0
    while indeks != -1:
        indeks = slowo.find(wzorzec, indeks + 1)
        licznik += 1
    return licznik

print(szukanie2(slowo,wzorzec))

def szukanie3(slowo, wzorzec):
    if len(wzorzec) > len(slowo):
        return False
    indeks = slowo.rfind(wzorzec)
    licznik = 0
    while indeks != -1:
        indeks = slowo.rfind(wzorzec, 0, indeks)
        licznik += 1
    return licznik

print(szukanie3(slowo,wzorzec))

