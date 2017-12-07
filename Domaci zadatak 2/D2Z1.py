#Domaci rad: Vezba br. 2 zadatak 1
#Funkcija koja racuna sumu elemenata niza na parnim pozicijama
def sumaParnih(niz):
    suma=0
    d=len(niz)
    i=1
    while i< d:
        suma=suma+niz[i]
        i=i+2
    return suma
#Glavni program!
niz=input("Unesite niz brojeva (pri unosu je potrebno  staviti zarez izmedju clanova niza) ")
suma1=sumaParnih(niz)
print "Suma parnih elemenata niza je=", suma1


