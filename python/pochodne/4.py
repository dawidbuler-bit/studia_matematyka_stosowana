import sympy
from sympy import *

x = symbols('x')

f = (5*x**4 - 3*x**3 - 2*x**2 - 7*x + 4)/x**2

x_0 = 1

styczna = f.subs(x,x_0)+diff(f).subs(x,x_0)*(x-x_0)

p = plot(styczna,(x,0,5,2) ,show=false)
p1 = plot(f,(x,0,5,2), show=false)

p1.extend(p)

p1.show()