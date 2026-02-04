import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

12.1(a)
x = np.linspace(-10,10, 200)
y = 1/(1+x**2)
plt.plot(x,y,'g', label = '1/(1+x^2)')
plt.legend()
plt.show()

12.1(b)
x = np.linspace(0,4)
y1 = x**2
y2 = np.exp(x)
y3 = x**x
plt.plot(x,y1, label = 'x^2')
plt.plot(x,y2, label = 'e^x')
plt.plot(x,y3, label = 'x^x')
plt.legend()
plt.show()

12.1(c)
x = np.linspace(0,3)
y1 = x**2
y2 = np.exp(x)
y3 = x**x
fig, axs = plt.subplots(3)
axs[0].plot(x,y1,'green',linestyle="--", label = 'x^2')
axs[0].set_ylim(0,25)
axs[1].plot(x,y2,'red',linestyle=':', label = 'e^x')
axs[1].set_ylim(0,25)
axs[2].plot(x,y3,'blue',  label = 'x^x')
axs[2].set_ylim(0,25)
fig.legend(title='Wykres',loc = "upper center")
plt.show()

12.2
titanic = pd.read_csv('titanic.csv', encoding = "UTF-8")

12.2 (a)
print(len(titanic[(titanic['Sex']=='female') & (titanic['Pclass']==1)& (titanic['Survived']==1)]))

12.2 (b)
print(np.mean(titanic[(titanic['Sex']=='male') &(titanic['Survived']==0)]['Age']))

12.2 (c)
colors = np.where(titanic['Sex']=='male','blue','red')
titanic.plot.scatter(x = 'Age', y = 'Fare', c = colors)
plt.show()

12.2 (d)
((titanic[titanic['Survived']==1]).groupby(['Pclass']).size()/
titanic.groupby(['Pclass']).size()).plot.bar()
plt.show()

12.3
dane = sns.load_dataset("iris")
print(dane)

12.3(a)
sns.relplot(x = 'sepal_length', y ='sepal_width',data = dane, kind = 'scatter', hue = 'species')
sns.catplot(x = 'species',y = 'petal_length', data = dane, kind = 'violin')
plt.show()

12.3(b)
sns.pairplot(dane, hue = 'species')
reg = stats.linregress(dane['petal_width'],dane['petal_length'])
print(reg)
x = np.linspace(0,3)
y = reg.intercept + x*reg.slope
plt.plot(x,y,'r')
plt.plot(dane['petal_width'], dane['petal_length'],'o')
plt.show()
