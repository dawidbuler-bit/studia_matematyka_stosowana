import numpy as np

A = np.array([[1, 1, 2],
              [2, 1, 0],
              [4, 1, 2]])

B = np.array([[2, 5, 7],
              [2, 8, 0],
              [4, 3, 1]])
print("A :\n", A)
print("B :\n", B)

print("A + B:\n", A + B)
print("A · B:\n", np.dot(A, B))
print("Iloczyn po-elementowy A i B:\n", A * B)
print("AT:\n", np.transpose(A))
print("A^-1:\n", np.linalg.inv(A))
print("Elementy A do 5-tej potęgi:\n", A**5)
print("A do piątej potęgi:\n", np.linalg.matrix_power(A, 5))
print("Det B:", np.linalg.det(B))
print("B do -3 potęgi:\n", np.linalg.matrix_power(B, -3))


C = np.array([[1],
              [2],
              [4]])
print("C :\n", C)

D = np.array([2, 5, 7])
print("D :\n", D)
print("C · D:\n", np.dot(C.T, D))
print("D · C:\n", np.dot(D.T, C))

E = np.array([[1, 5],
              [2, 1]])
print("E :\n", E)

F = np.array([[2, 1],
              [2, 8]])
print("F :\n", F)