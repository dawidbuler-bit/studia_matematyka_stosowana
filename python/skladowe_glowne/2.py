import pandas as pd
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns


plik = r"D:\pythonProject6\mtcars.csv"

data = pd.read_csv(plik)

numdata = data[['mpg', 'cylinders', 'disp', 'hp', 'drat', 'wt', 'qsec', 'gear', ' carb']]

pca = PCA(n_components=2)
pca.fit(scale(X))
print(pca.components_)#e.v
print(sum(pca.explained_variance_ratio_))#%of information
T = pca.transform(scale(numdata)).round(2))

print(T)

data['First component'] = T[:,0]
data['Second component'] = T[:,1]

print(data)

sns.scattterplot(data = data, x = 'First component', y = 'Second component', hue='model')

plt.show()




