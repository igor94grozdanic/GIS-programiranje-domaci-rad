#Domaci rad: Vezba br. 2 zadatak 3
#Funkcija koja racuna proizvod elemenata niza
def proizvodElemenata(niz):
    suma=1
    d=len(niz)
    i=0
    while i< d:
        suma=suma*niz[i]
        i=i+1
    return suma
#Glavni program!
niz=input("Unesite niz brojeva (pri unosu je potrebno  staviti zarez izmedju clanova niza)  ")
pr1=proizvodElemenata(niz)
print "Proizvod elemenata niza je=", pr1