from sympy import *
import sympy

x = sympy.symbols('x')

f = sin(x)**3/(sin(x)**3 + cos(x)**3)

F = integrate(f)

plot(F.subs(0,pi/2))
