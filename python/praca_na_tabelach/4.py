import numpy as np

imiona = np.array(['Anna','Zofia','Sylwia','Katarzyna','Teresa','Tomasz','Cezary','Zenon','Filip','Adrian'])
age = np.array([20,30,21,34,45,21,17,18,19,23,36,69,34,58,23,44,12])
sex = np.array(['M','K','M','M','K','M','K','M','K','M','M','K','K',
'M','M','K','M'])
waga = np.array([65,80,64,69,74,61,66,61,69,77])
wzrost = np.array([179,179,151,177,170,157,151,153,160,160])
okulary = np.array(['NIE','TAK','NIE','TAK','NIE','TAK','NIE','TAK','NIE','TAK'])

print(np.sort(imiona))



print(imiona[age >= 20 and age <= 30 and sex == K])