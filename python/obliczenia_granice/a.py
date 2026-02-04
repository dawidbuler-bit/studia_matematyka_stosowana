import sympy
import math

n = sympy.symbols('n')
print(sympy.limit(sympy.sqrt(n+5)-sympy.sqrt(n),n,+math.inf).doit())



