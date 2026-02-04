import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.array([0, 1, 2, 3, 4, 5])
y= np.array([2.1, 7.7, 13.6, 27.2, 40.9, 61.1])

def kwardatowa(x,y):
    n = len(x)
    beta = np.polyfit(x, y, 2)[::-1]
    yhat = beta[0] + beta[1] * x + beta[2] * x ** 2
    z = np.linspace(min(x), max(x))
    plt.plot(z, beta[0] + z * beta[1] + z ** 2 * beta[2],'r')
    plt.plot(x, y,'o')
    r = np.sum((yhat - np.mean(y)) ** 2) /(np.sum((y - np.mean(y)) ** 2))
    wsp = 1 - r**2
    return plt.show(), wsp

print(kwardatowa(x,y))

