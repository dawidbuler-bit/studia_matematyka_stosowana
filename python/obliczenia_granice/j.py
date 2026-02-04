import sympy as sp

n = sp.symbols('n')

print(sp.limit((1+sp.tan((6*n)/(4*(n**2)-1)))**(5*n),n,sp.oo).doit())