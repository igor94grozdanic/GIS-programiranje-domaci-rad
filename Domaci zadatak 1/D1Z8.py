#Domaci rad: Vezba 1 zadatak 8
import random

a=int(random.uniform(0,100))
ime=raw_input("Unesite vase ime: ")
t=1
br=0
while (t==1):
    s=int(input("Unesite broj   "))
    if (s==a):
        print 'Pogodili ste!!!  '
        print 'Broj vasih pokusaja je ',br
        t=0
    elif (s<a):
        print 'Broj koji ste uneli je manji od broja koji je racunar zamislio.'
        br+=1
    else:
        print 'Broj koji ste uneli je veci od broja koji je racunar zamislio.'
        br+=1


