import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import scale
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch


plik = r"D:\pythonProject6\16.01\mtcars.csv"
data = pd.read_csv(plik)


numdata = data[['mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']].to_numpy()

car_names = [
    "Mazda RX4", "Mazda RX4 Wag", "Datsun 710", "Hornet 4 Drive", "Hornet Sportabout", "Valiant",
    "Duster 360", "Merc 240D", "Merc 230", "Merc 280", "Merc 280C", "Merc 450SE", "Merc 450SL", "Merc 450SLC",
    "Cadillac Fleetwood", "Lincoln Continental", "Chrysler Imperial", "Fiat 128", "Honda Civic",
    "Toyota Corolla", "Toyota Corona", "Dodge Challenger", "AMC Javelin", "Camaro Z28", "Pontiac Firebird",
    "Fiat X1-9", "Porsche 914-2", "Lotus Europa", "Ford Pantera L", "Ferrari Dino", "Maserati Bora", "Volvo 142E"]


kmeans = KMeans(n_clusters=5, random_state=0).fit(numdata)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_



clustering = AgglomerativeClustering(n_clusters=5, linkage='ward')
clustering.fit(numdata)

# Rysowanie dendrogramu
plt.figure(figsize=(10, 7))
sch.dendrogram(sch.linkage(numdata, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Samochody')
plt.ylabel('Odległość')
plt.xticks(np.arange(0, len(car_names), step=5), car_names[::5], rotation=90)
plt.show()