import sympy
from sympy import *

x = symbols('x')

f = (5*x**4 - 3*x**3 - 2*x**2 - 7*x + 4)/x**2

print(diff(f).subs(x,1))
