import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import scale
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA


iris = load_iris()
X = iris.data

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

kmeans_3 = KMeans(n_clusters=3, random_state=42)
labels_3 = kmeans_3.fit_predict(X)


kmeans_6 = KMeans(n_clusters=6, random_state=42)
labels_6 = kmeans_6.fit_predict(X)



plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels_3, cmap='viridis')
plt.title('Klasteryzacja k-średnich (3 klastry)')
plt.xlabel('Pierwsza składowa główna')
plt.ylabel('Druga składowa główna')

plt.subplot(1, 2, 2)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels_6, cmap='viridis')
plt.title('Klasteryzacja k-średnich (6 klastrów)')
plt.xlabel('Pierwsza składowa główna')
plt.ylabel('Druga składowa główna')


plt.tight_layout()
plt.show()