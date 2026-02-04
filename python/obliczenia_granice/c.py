import sympy as sp
import math

n = sp.symbols('n')
print(sp.limit(sp.sqrt(3*(n**2) + 2*n - 5) - n*sp.sqrt(3),n,+math.inf).doit())