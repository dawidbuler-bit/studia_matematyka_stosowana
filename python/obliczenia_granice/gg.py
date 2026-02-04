import sympy as sp

n = sp.symbols('n')

print(sp.limit((((n**2)+5)/(n**2 -4))**((n**2)+3), n, sp.oo).doit())