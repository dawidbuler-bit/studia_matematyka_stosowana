import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sympy import symbols

x1 = np.array([10,8,13,9,11,14,6,4,12,7,5])
x2 = np.array([10,8,13,9,11,14,6,4,12,7,5])

x3 = np.array([10,8,13,9,11,14,6,4,12,7,5])
x4 = np.array([8,8,8,8,8,8,8,19,8,8,8])

y1 = np.array([8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.86])
y2 = np.array([9.14,8.14,8.74,8.77,9.26,8.10,6.13,3.10,9.13,7.26,4.74])

y3 = np.array([7.46,6.77,12.74,7.11,7.81,8.84,6.08,5.39,8.15,6.42,5.73])
y4 = np.array([6.58, 5.76, 7.71,8.84,8.47,7.04,5.25,12.50,5.56,7.91,6.89])


def kwartet(x,y):

    n = len(x)

    beta2 = (n*sum(x*y) - sum(x)*sum(y))/(n*sum(x**2) - (sum(x))**2)

    beta1 = (sum(y) - beta2*sum(x))/n

    a = np.linspace(0,20)
    b = beta1 + a*beta2
    reg = stats.linregress(x, y)
    plt.plot(a, b, 'r')
    plt.plot(x, y, 'o')

    return np.polyfit(x, y, 1) , reg , plt.show()

print(kwartet(x1, y1))
print(kwartet(x2, y2))
print(kwartet(x3, y3))
print(kwartet(x4, y4))



def kwardatowa(x,y):
    n = len(x)
    beta = np.polyfit(x, y, 2)[::-1]
    yhat = beta[0] + beta[1] * x + beta[2] * x ** 2
    print(yhat)
    print(np.sum((yhat - np.mean(y)) ** 2) , np.sum((y - np.mean(y)) ** 2))
    z = np.linspace(min(x), max(x))
    plt.plot(z, beta[0] + z * beta[1] + z ** 2 * beta[2],'r')
    plt.plot(x, y,'o')
    return plt.show()



print(kwardatowa(x1,y1))
print(kwardatowa(x2,y2))
print(kwardatowa(x3,y3))
print(kwardatowa(x4,y4))






