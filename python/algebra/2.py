import numpy as np

A_1 = np.array([[2, -3],[5, 1]])
b_1 = np.array([4, -2])

A_2 = np.array([[1,1,1],[2,3,1],[1,1,3]])
b_2 = np.array([3,6,3])

A_3 = np.array([[2,-3,1],[1,-1,1],[3,0,-4]])
b_3 = np.array([-1,1,0])
def cramer(A, b):
    pierwiastki = []
    for i in range(0,len(b)):
        A_x = A.copy()
        A_x[:, i] = b
        d = np.linalg.det(A)
        p = np.linalg.det(A_x) / d
        pierwiastki.append(p)
    return pierwiastki


print(cramer(A_3, b_3))

import sympy as sp

A_1 = sp.Matrix([[2, -3],[5, 1]])
b_1 = sp.Matrix([4, -2])

A_2 = sp.Matrix([[1,1,1],[2,3,1],[1,1,3]])
b_2 = sp.Matrix([3,6,3])

A_3 = sp.Matrix([[2,-3,1],[1,-1,1],[3,0,-4]])
b_3 = sp.Matrix([-1,1,0])
def cramer_2(A, b):
    pierwiastki = []
    for i in range(0,len(b)):
        A_x = A.copy()
        A_x[:, i] = b
        d = A.det()
        p = A_x.det() / d
        pierwiastki.append(p)
    return pierwiastki

print(cramer_2(A_3, b_3))

