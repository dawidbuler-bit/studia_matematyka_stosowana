import sympy
from sympy import *

x = symbols('x')

f = (3*x + sin(x))**2

print(diff(f).subs(x,pi/2), diff(f).subs(x,5))