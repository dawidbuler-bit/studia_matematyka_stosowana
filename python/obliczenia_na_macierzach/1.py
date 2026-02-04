import numpy as np

my_array = np.arange(10, 40, 2)


print(my_array[:]+3)

print(my_array[:]*2)

c = my_array[my_array % 6 == 2] = 0

print(my_array)

resized = my_array.reshape(-1,1)

print(resized ,my_array.shape)

A = np.arange([1,0,2,0,3,0,4,0])
x = "x"

def change(A, x):
    B = np.copy(A)
    B[B == 0] = x
    return B

zmieniony = change(A , x)

print(zmieniony)

