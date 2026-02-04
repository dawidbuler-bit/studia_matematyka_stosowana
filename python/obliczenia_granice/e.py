import sympy as sp
import math


n = sp.symbols('n')
print(sp.limit(n/(sp.factorial(n))**(1/n),n,+math.inf).doit())

