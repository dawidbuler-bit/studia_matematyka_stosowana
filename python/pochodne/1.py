import sympy
from sympy import *

x = symbols('x')

f1 = x**3 - 2*x

f2 = 3*(x**2)

print(diff(f1).subs(x,3),diff(f2).subs(x,3))
