def deszyfr(tekst):
    n = len(tekst)
    plotek1 = (n+3) // 4
    plotek2 = n // 2
    plotek3 = (n+1) // 4
    czesc1 = tekst[:plotek1]
    czesc2 = tekst[plotek1:plotek1+plotek2]
    czesc3 = tekst[plotek1+plotek2:]
    wynik = ['' for _ in range(n)]
    for i in range(len(czesc1)):
        wynik[i*4] = czesc1[i]
    for i in range(len(czesc2)):
        wynik[1+i*2] = czesc2[i]
    for i in range(len(czesc3)):
        wynik[2+i*4] = czesc3[i]
    return ''.join(wynik)

print(deszyfr("KTAARPONLZYAI"))


def cezar(tekst,alfabet, klucz):
    wynik = ''
    dlt = len(tekst)
    dla = len(alfabet)
    for i in range(dlt):
        if tekst[i] == alfabet[alfabet.find(tekst[i])]:
            wynik += alfabet[(alfabet.find(tekst[i]) + klucz) % dla]
    return wynik

print(cezar("kryptoanaliza",'abcdefghijklmnopqrstuvwxyz',3))

def mono(tekst,alfabet):
    tekst = tekst.replace(' ', '').upper()
    alfabet2 = ''
    for i in range(len(tekst)):
        if not (tekst[i] in alfabet2):
            alfabet2 += tekst[i]
    for i in range(len(alfabet)):
        if not (alfabet[i] in alfabet2):
            alfabet2 += alfabet[i]
    return alfabet2

print(mono('kazdy jest kowalem swego losu','ABCDEFGHIJKLMNOPQRSTUVWXYZ' ))


def onom(tekst, alfabet):
    tekst = tekst.replace(' ', '').upper()
    alfabet2 = ''
    ALFABET3 = ''
    for i in range(len(tekst)):
        if not (tekst[i] in alfabet2):
            alfabet2 += tekst[i]
    for i in range(len(alfabet2)-1,0,-1):
        ALFABET3 += alfabet2[i]
        print(ALFABET3)
    for i in range(len(alfabet)):
        if not (alfabet[i] in ALFABET3):
            ALFABET3 += alfabet[i]
    return ALFABET3


print(onom('WOBEC FAKTOW ARGUMENTY MUSZA USTAPIC', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
