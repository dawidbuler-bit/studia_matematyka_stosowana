from math import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
x = np.linspace(-5,5)
def f(x, mu = 0, sigma2 = 1):
    sigma = sqrt(sigma2)
    return norm.cdf(x, mu, sigma2)
y1 = np.array([f(i) for i in x])
y2 = np.array([f(i,0,0.2) for i in x])
y3 = np.array([f(i,0,5) for i in x])
y4 = np.array([f(i,-2,0.5) for i in x])
plt.plot(x,y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x,y4)
plt.show()