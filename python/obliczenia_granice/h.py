import sympy as sp

n = sp.symbols('n')

print(sp.limit(((2*(n**2) - n + 2)/(2*(n**2)+1))**((3*n)-1),n,sp.oo).doit())