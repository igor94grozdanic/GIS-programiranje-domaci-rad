#Domaci rad: Vezba br. 2 zadatak 2
#Funkcija koja racuna sumu elemenata niza
def sumaElemenata(niz):
    suma=0
    d=len(niz)
    i=0
    while i< d:
        suma=suma+niz[i]
        i=i+1
    return suma
#Glavni program!
niz=input("Unesite niz brojeva (pri unosu je potrebno  staviti zarez izmedju clanova niza) ")
suma1=sumaElemenata(niz)
print "Suma elemenata niza je=", suma1