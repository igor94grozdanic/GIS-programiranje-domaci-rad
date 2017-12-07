#Domaci rad: Vezba br. 2 zadatak 4
#Funkcija koja kreira novi niz.
def noviNiz(niz1,niz2):
    nov=[]
    n1=len(niz1)
    n2=len(niz2)
    i=0
    k=0
    if n1<n2:
        while i<n1:
            nov.insert(k,niz1[i])
            k=k+1
            nov.insert(k, niz2[i])
            i=i+1
            k=k+1
        while i<n2:
            nov.insert(k, niz2[i])
            i+=1
            k+=1
    elif n1>n2:
        while i<n2:
            nov.insert(k, niz1[i])
            k=k+1
            nov.insert(k, niz2[i])
            i=i+1
            k=k+1
        while i<n1:
            nov.insert(k, niz1[i])
            i+=1
            k+=1
    else:
        while i<n1:
            nov.insert(k, niz1[i])
            k=k+1
            nov.insert(k, niz2[i])
            i=i+1
            k=k+1
    return nov

#Glavni program!
niz1=input("Unesite prvi niz (pri unosu je potrebno  staviti zarez izmedju clanova niza) ")
niz2=input("Unesite drugi niz (pri unosu je potrebno  staviti zarez izmedju clanova niza) ")
opcija=raw_input("Unesite opciju (p-prvi niz ili d-drugi niz) ")
proba=[]
if opcija=="p":
    proba=noviNiz(niz1, niz2)
elif opcija=="d":
    proba=noviNiz(niz2,niz1)
else:
    print"pogresna opcija"
j=0
s=len(proba)
while j<s:
    print (proba[j])
    j=j+1
