import sympy as sp
import math

n = sp.symbols('n')
print(sp.limit(sp.sin(n)/(n+3),n,+math.inf).doit())


