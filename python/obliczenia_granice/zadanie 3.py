import math
from math import *
import sympy
from sympy import *

#a
x = symbols('x')
print(limit((x**2 + x + 1)/(2*x**2 + x + 3), x, +oo).doit())

#b
print(limit((x**2 + x +1)/(2*x**2 + x + 3), x, 0).doit())

#c
print(limit((log(x+1))/(x-1), x, 0).doit())

#d
print(limit((sin(x))/(x+3), x, 0).doit())
