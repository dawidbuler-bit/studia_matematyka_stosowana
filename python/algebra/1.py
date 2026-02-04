import sympy as sp
import numpy as np

A = [[2, 0, 3, -1],[1, -1, 2, 3],[3, 2, 0, 2],[4, 1, 5, 1]]

print(np.linalg.det(np.array(A)))


print(sp.Matrix(A).det())
