import sympy as sp
import math

n = sp.symbols('n')
print(sp.limit((2**n + 8**n +11**n)**(1/n),n,+math.inf).doit())