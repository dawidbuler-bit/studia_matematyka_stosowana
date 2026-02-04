import math
from math import *
import sympy
from sympy import *

k, n = symbols('k n')

suma_a = Sum(1/(2**k), (k, 0, +00)).doit()
print(suma_a)
#.subs(n, 10) i tak dalej

suma_b = Sum((2**k)/factorial(k), (k, 0, +oo)).doit()
print(suma_b)

suma_c = Sum(1/k**2, (k, 1, +oo)).doit()
print(suma_c)

suma_d = Sum((3+2*k)/(2**k), (k, 1, +oo)).doit()
print(suma_d)

