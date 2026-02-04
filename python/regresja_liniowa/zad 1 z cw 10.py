import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

'''
x = np.array([-1, 0, 1 ,2, 3])
y = np.array([-3, -1, 1, 3, 5])

n = len(x)

beta2 = (n*sum(x*y) - sum(x)*sum(y))/(n*sum(x**2) - (sum(x))**2)

beta1 = (sum(y) - beta2*sum(x))/n

a = np.linspace(-10,20)
b = beta1 + a*beta2

print(np.polyfit(x, y, 1))
reg= stats.linregress(x, y)
print(reg)

plt.plot(a, b, 'r')
plt.plot(x, y, 'o')
plt.show()
'''

x = np.array([0, 0.5, 0.9, 1.6, 2])
y = np.array([1, 2.5, 4, 6, 7.1])

n = len(x)

beta2 = (n*sum(x*y) - sum(x)*sum(y))/(n*sum(x**2) - (sum(x))**2)

beta1 = (sum(y) - beta2*sum(x))/n

a = np.linspace(-10,20)
b = beta1 + a*beta2

print(np.polyfit(x, y,1))
reg= stats.linregress(x, y)
print(reg)

plt.plot(a, b, 'r')
plt.plot(x, y, 'o')
plt.show()
