import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd


penguins = sns.load_dataset('penguins')
penguins = penguins.dropna()  # Usunięcie brakujących danych

X_penguins = penguins[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]

# Redukcja wymiarów do dwóch składowych głównych
pca = PCA(n_components=2)
X_penguins_pca = pca.fit_transform(X_penguins)


kmeans_penguins = KMeans(n_clusters=3, random_state=42)
kmeans_penguins_labels = kmeans_penguins.fit_predict(X_penguins)


plt.figure(figsize=(6, 6))
plt.scatter(X_penguins_pca[:, 0], X_penguins_pca[:, 1], c=kmeans_penguins_labels, cmap='viridis')
plt.title('Klasteryzacja k-średnich (3 klastry) dla pingwinów')
plt.xlabel('Pierwsza składowa główna')
plt.ylabel('Druga składowa główna')


plt.colorbar(label='Numer klastra')
plt.show()

# Porównanie z rzeczywistymi gatunkami pingwinów
labels_true = penguins['species'].astype('category').cat.codes  # Kodowanie gatunków jako liczby
comparison = pd.crosstab(labels_true, kmeans_penguins_labels, rownames=['Gatunek'], colnames=['Klastr'])
print(comparison)
