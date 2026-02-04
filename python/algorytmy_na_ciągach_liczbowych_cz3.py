
#zad 1
def babel(T):
    n = len(T)
    print(T)
    for j in range(n-1, 0, -1):
        for i in range(j):
            if T[i] > T[i+1]:
                T[i], T[i+1] = T[i+1], T[i]
                print(T)
    return T

print(babel([5,4,3,2,1,0]))

#zad 2
def wstawianie(T):
    n = len(T)
    print(T)
    for i in range(1, n):
        temp = T[i]
        k = i - 1
        while k >= 0 and T[k] > temp:
            T[k+1] = T[k]
            k -= 1
        T[k+1] = temp
        print(T)
    return T



print(wstawianie([2, 4, 6, 8, 3, 1, 6, 8, 9, 0]))


#zad 3
def najjwiekszy(T):
    n = len(T)
    temp = []
    while len(T) > 1:
        for i in range(0, n-1 , 2):
            temp.append(max(T[i], T[i+1]))
    if n % 2 == 1:
        temp.append(T[-1])

    T = temp

    return T[0]

print(max([2,5,1,8,3,9,1]))



#zad 4
def podziel(T):
    mniejsze = []
    wieksze = []
    for i in range(0, len(T) - 1, 2):
        if T[i] < T[i + 1]:
            mniejsze.append(T[i])
            wieksze.append(T[i + 1])
        else:
            mniejsze.append(T[i + 1])
            wieksze.append(T[i])
    if len(T) % 2 == 1:
        wieksze.append(T[-1])
        mniejsze.append(T[-1])
    return mniejsze, wieksze


def min_max(T):
    if not T:
        return None, None
    mniejsze = T[:]
    wieksze = T[:]
    while len(mniejsze) > 1:
        mniejsze, _ = podziel(mniejsze)
    while len(wieksze) > 1:
        _, wieksze = podziel(wieksze)
    return mniejsze[0], wieksze[0]


T = [1, 5, 7, 3, 9, 11, 13]

print(min_max([1, 5, 7, 3, 9, 11, 13]))


#zad 5

def znajdz_min_max(T):

    def podziel_i_znajdz(T, lewy, prawy):
        if lewy == prawy:
            return T[lewy], T[lewy]

        if prawy == lewy + 1:
            if T[lewy] < T[prawy]:
                return T[lewy], T[prawy]
            else:
                return T[prawy], T[lewy]

        srodek = (lewy + prawy) // 2
        min1, max1 = podziel_i_znajdz(T, lewy, srodek)
        min2, max2 = podziel_i_znajdz(T, srodek + 1, prawy)

        return min(min1, min2), max(max1, max2)

    if not T:
        return None, None

    return podziel_i_znajdz(T, 0, len(T) - 1)

T = [1, 5, 7, 3, 9, 11, 13]
print(znajdz_min_max(T))


#zad 6

def szybkie_sortowanie(T):

    if len(T) <= 1:
        return T

    lewa = []
    prawa = []
    for i in range(1, len(T)):
        if T[i] < T[0]:
            lewa.append(T[i])
        else:
            prawa.append(T[i])

    return szybkie_sortowanie(lewa) + [T[0]] + szybkie_sortowanie(prawa)



T = [9, 3, 7, 5, 1, 6, 8, 2, 4]
posortowane = szybkie_sortowanie(T)
print(posortowane)
