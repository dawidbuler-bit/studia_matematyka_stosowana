import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, cut_tree
from sklearn.preprocessing import scale


data = pd.read_csv("D:\pythonProject6\16.01\mtcars.csv",index_col = 0)

print(data)

newdata = pd.DataFrame(scale(data), index=data.index,
columns=data.columns)
linkage_data = linkage(newdata, method='ward', metric='euclidean')
dendrogram(linkage_data,labels = newdata.index, truncate_mode = 'lastp', p=5)
cutree = cut_tree(linkage_data, n_clusters=5)
print(cutree)
print(pd.DataFrame(cutree, index=data.index,))
plt.show()