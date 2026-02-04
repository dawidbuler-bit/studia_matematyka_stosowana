import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


points = np.array([[2, 3], [6, 1], [1, 2], [3, 0], [4, 2], [2, 7], [4, 9]])


kmeans = KMeans(n_clusters=2, random_state=0).fit(points)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_


plt.figure(figsize=(8, 12))
for i, color in enumerate(['red', 'blue']):
    cluster_points = points[labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], color=color, label=f'Cluster {i+1}')


plt.scatter(centroids[:, 0], centroids[:, 1], color='green', marker='X', s=100, label='Centroids')

plt.title('Podział punktów na dwa klastry (k-means)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
