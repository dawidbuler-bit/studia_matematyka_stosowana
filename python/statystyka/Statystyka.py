'''
import numpy as np
from scipy.stats import *


imiona = np.array(['Anna','Zofia','Sylwia','Katarzyna','Teresa','Tomasz','Cezary','Zenon','Filip','Adrian'])
age = np.array([20,30,21,34,45,21,17,18,19,23,36,69,34,58,23,44,12])
sex = np.array(['M','K','M','M','K','M','K','M','K','M','M','K','K',
'M','M','K','M'])
waga = np.array([65,80,64,69,74,61,66,61,69,77])
wzrost = np.array([179,179,151,177,170,157,151,153,160,160])
okulary = np.array(['NIE','TAK','NIE','TAK','NIE','TAK','NIE','TAK','NIE','TAK'])

print("\n")
print("Średnia arytmetyczna wieku wynosi: ",pmean(age, p=1))
print("Średnia geometrycza wieku wynosi: " ,gmean(age))
print("Średnia harmoniczna wieku wynosi: " ,hmean(age))
print("Średnia ważona wieku wynosi: " ,np.average(age))
print("\n")
print("Średnia arytmetyczna wagi wynosi: ",pmean(waga, p=1))
print("Średnia geometrycza wagi wynosi: " ,gmean(waga))
print("Średnia harmoniczna wagi wynosi: " ,hmean(waga))
print("Średnia ważona wagi wynosi: " ,np.average(waga))
print("\n")
print("Średnia arytmetyczna wzrostu wynosi: ",pmean(wzrost, p=1))
print("Średnia geometrycza wzrostu wynosi: " ,gmean(wzrost))
print("Średnia harmoniczna wzrostu wynosi: " ,hmean(wzrost))
print("Średnia ważona wzrostu wynosi: " ,np.average(wzrost))
print("\n")
print("\n")


print("Dla wieku: ",mode(age))
print("\n")
print("Dla wagi: ",mode(waga))
print("\n")
print("Dla wzrostu: ",mode(wzrost))
print("\n")
print("\n")


print("Dla wieku:")
print("Pierwszy kwantyl wynosi: ",np.quantile(age,0.25))
print("Drugi kwantyl wynosi: ",np.quantile(age,0.5))
print("Trzeci kwantyl wynosi: ",np.quantile(age,0.75))
print("\n")
print("Dla wagi:")
print("Pierwszy kwantyl wynosi: ",np.quantile(waga,0.25))
print("Drugi kwantyl wynosi: ",np.quantile(waga,0.5))
print("Trzeci kwantyl wynosi: ",np.quantile(waga,0.75))
print("\n")
print("Dla wzrostu:")
print("Pierwszy kwantyl wynosi: ",np.quantile(wzrost,0.25))
print("Drugi kwantyl wynosi: ",np.quantile(wzrost,0.5))
print("Trzeci kwantyl wynosi: ",np.quantile(wzrost,0.75))
print("\n")
print("\n")

print("Miary zmienności klasyczne dla wieku:")
print("Odchylenie przeciętne: ",sum(abs(age-np.mean(age)))/len(age))
print("Wariancja: ",np.var(age))
print("Odchylenie standardowe: ",np.std(age))
print("\n")
print("Miary zmienności klasyczne dla wagi:")
print("Odchylenie przeciętne: ",sum(abs(waga-np.mean(waga)))/len(waga))
print("Wariancja: ",np.var(waga))
print("Odchylenie standardowe: ",np.std(waga))
print("\n")
print("Miary zmienności klasyczne dla wzrostu:")
print("Odchylenie przeciętne: ",sum(abs(wzrost-np.mean(wzrost)))/len(wzrost))
print("Wariancja: ",np.var(wzrost))
print("Odchylenie standardowe: ",np.std(wzrost))
print("\n")
print("\n")

print("Miary zmienności pozycyjne dla wieku: ")
print("Rozstęp: ",max(age)-min(age))
print("Rozstęp ćwiartkowy: ",np.quantile(age,0.75)-np.quantile(age,0.25))
print("Odchylenie ćwiartkowe ",(np.quantile(age,0.75)-np.quantile(age,0.25))/2)
print("\n")
print("Miary zmienności pozycyjne dla wagi: ")
print("Rozstęp: ",max(waga)-min(waga))
print("Rozstęp ćwiartkowy: ",np.quantile(waga,0.75)-np.quantile(waga,0.25))
print("Odchylenie ćwiartkowe ",(np.quantile(waga,0.75)-np.quantile(waga,0.25))/2)
print("\n")
print("Miary zmienności pozycyjne dla wzrostu: ")
print("Rozstęp: ",max(wzrost)-min(wzrost))
print("Rozstęp ćwiartkowy: ",np.quantile(wzrost,0.75)-np.quantile(wzrost,0.25))
print("Odchylenie ćwiartkowe ",(np.quantile(wzrost,0.75)-np.quantile(wzrost,0.25))/2)
print("\n")

'''

#zad 2

import matplotlib.pyplot as plt
from sympy import *

t, x = symbols('t, x')

def f(x, mu = 0, sigma2 = 1):
    sigma = sqrt(sigma2)
    return 1/(sigma*sqrt(2*pi))*exp(-(x-mu)**2/(2*sigma**2))

def F(x, mu = 0, sigma2 = 1):
    return integrate(f(t, mu, sigma2),(t,-oo,x))

p1 = plot(F(x), xlim=[-7,7], show=False)
p2 = plot(F(x, 0,0.2), show=False)
p3 = plot(F(x, 0, 5), show=False)
p4 = plot(F(x, -2, 0.5), show=False)
p1.extend(p2)
p1.extend(p3)
p1.extend(p4)
p1.show()
