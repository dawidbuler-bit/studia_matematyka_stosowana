import sympy as sp
import math

n = sp.symbols('n')
print(sp.limit(((((n+1)**(n+1))/(n**n)) - ((n**n)/((n-1)**(n-1)))),n,sp.oo).doit())