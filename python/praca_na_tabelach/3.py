import numpy as np

rozmiar_buta = np.array([5, 6, 6, 6, 5, 7, 6, 5, 6, 7, 7, 6, 7, 10,
9.5, 10, 10, 9, 10.5, 9.5, 8.5, 9, 10, 8,
10, 9, 12, 11, 9, 10, 11, 11, 12, 10.5, 11.5,
11, 13, 12, 12.5, 13])
wzrost = np.array([153, 154, 154, 155, 158, 159, 160, 161, 163,
164, 165, 165, 165, 166, 167, 167, 168, 168,
170, 170, 170, 171, 173, 174, 174, 174, 175,
175, 176, 177, 178, 178, 178, 179, 179, 179,
180, 180, 183,185])

#a)
print(max(rozmiar_buta))

#b)
print(np.mean(wzrost[rozmiar_buta == max(rozmiar_buta)]))

#c)
print(min(wzrost[rozmiar_buta == max(rozmiar_buta)]))

#d)
print(np.mean(rozmiar_buta))

#e)
print(min(wzrost[rozmiar_buta==10]),max(wzrost[rozmiar_buta==10]))

#f)
rozmiar_buta += 32
print(np.array([rozmiar_buta]))