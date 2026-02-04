import sympy as sp

n = sp.symbols('n')

print(sp.limit((((4**(n+3)-7)/(2**(2*n +4)+1))**(3*n -1)),n,sp.oo).doit())