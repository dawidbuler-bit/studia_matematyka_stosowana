import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

dl_x = np.array([80, 90, 100 ,100 ,110 , 120])
koszt = np.array([12, 9, 10, 9, 8, 6])

n = len(dl_x)

beta2 = (n*sum(dl_x*koszt) - sum(dl_x)*sum(koszt))/(n*sum(dl_x**2) - (sum(dl_x))**2)

beta1 = (sum(koszt) - beta2*sum(dl_x))/n

a = np.linspace(0,150)
b = beta1 + a*beta2

print(np.polyfit(dl_x, koszt, 1))
reg= stats.linregress(dl_x, koszt)
print(reg)

plt.plot(a, b, 'r')
plt.plot(dl_x, koszt, 'o')
plt.show()


produkcja = np.array([11, 12, 13, 13, 14, 14, 17, 18, 18, 20])
koszty = np.array([18, 20, 20, 20, 22, 24, 26, 27, 26, 27])

n = len(produkcja)

beta2 = (n*sum(produkcja*koszty) - sum(produkcja)*sum(koszty))/(n*sum(produkcja**2) - (sum(produkcja))**2)

beta1 = (sum(koszty) - beta2*sum(produkcja))/n

a = np.linspace(0,30)
b = beta1 + a*beta2

print(np.polyfit(produkcja, koszty, 1))
reg= stats.linregress(produkcja, koszty)
print(reg)

plt.plot(a, b, 'r')
plt.plot(produkcja, koszty, 'o')
plt.show()
