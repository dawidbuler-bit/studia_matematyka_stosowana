
import pandas as pd


netflix.rating.isnull().sum()


netflix = netflix.dropna(subset = ["rating","country"])



netflix["type"].value_counts()



import matplotlib.pyplot as plt
import seaborn as sns

plt.figure()
(netflix["release_year"]).plot.hist()
plt.show()


plt.figure()
sns.histplot(data = netflix, x = "release_year")
plt.show()




df = netflix["rating"].value_counts()
df[df == df.max()].index(0)
df[df == df.max()].iloc(0)


df.sort_values().idmax()
df.sort_values().max()
