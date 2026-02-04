import sympy as sp

A = sp.Matrix([[0, 1],[1, 0]])

B = sp.Matrix([[4, 0],[0, 2]])

C = sp.Matrix([[4, 2],[-1, 2]])

D = sp.Matrix([[1, 2, 0],[0, 2, 0],[-2, -2, -1]])

x, y, z = sp.symbols('x, y, z')

print(A.eigenvects())
print(B.eigenvects())
print(C.eigenvects())
print(D.eigenvects())

import numpy as np

A = np.array([[0, 1],[1, 0]])
print(np.linalg.eig(A))