import numpy as np
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA

A = np.array([[1, 3, 2, 4, 5],
               [5, 6, 7, 1, 2],
               [3, 3, 4, 5, 7],
               [8, 9, 10, -2, -3],
               [4, 2, 1, 0, 7],
               [5, 2, 0, -1, 7]])

m = len(A.transpose())
n = len(A)

u = np.mean(A, axis=0)
w = np.array([(np.var(A[:,i]))**(1/2) for i in range(m)])

U = np.meshgrid(u,np.ones(n))[0]
W = np.meshgrid(w,np.mean(n))[0]

B = (A - U)/W

print("Macierz odchyleń: ", "\n","\n", B)

C = (1/n)*B.transpose()@B
V = np.linalg.eig(C)[1]


print("\n","Macierz kowariancji: ","\n","\n", C,"\n","\n")
print("\n","Macierz V (wektory własne): ""\n","\n",V,"\n","\n")


print("Wartości własne: ", np.linalg.eig(C)[0],"\n","\n")

print(sum(np.linalg.eig(C)[0]))

D = np.linalg.inv(V)@C@V

print("\n","Macierz D: ","\n","\n",D.round(2),"\n","\n")

W = V[:,0:2]
T = B@W
print(T.round(2))

pca = PCA(n_components=2)
pca.fit(scale(X))
print(pca.components_)#e.v
print(sum(pca.explained_variance_ratio_))#%of information
print(pca.transform(scale(X)).round(2))

#wynik 97%
