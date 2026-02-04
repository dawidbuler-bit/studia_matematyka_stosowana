def babel(T):
    n = len(T)
    for j in range(n-1, 0, -1):
        for i in range(j):
            if T[i] > T[i+1]:
                T[i], T[i+1] = T[i+1], T[i]
    return T

print(babel([5,4,3,2,1,0]))

def wstawianie(T):
    n = len(T)
    for i in range(1, n):
        temp = T[i]
        k = i - 1
        while k >= 0 and T[k] > temp:
            T[k+1] = T[k]
            k -= 1
        T[k+1] = temp
    return T



print(wstawianie([2, 4, 6, 8, 3, 1, 6, 8, 9, 0]))

def max(T):
    n = len(T)
    temp = []
    while len(T) > 1:
        for i in range(0, n, 2):
            if T[i] > T[i+1]:
                temp.append(T[i])
        temp.append(T[i+1])


print(max([2,5,1,8,3,9,1]))

#temp.append(T(len(T)-1))

temp.append(T[-1])

T = temp

n % 2 != 0

return T