#Domaci rad: Vezba 1 zadatak 5
a=input("Unesite petocifreni broj: ")
a1=float(a)
i=0
max=0
d=10.0
while i<5:
    c=a1-(a1//d)*d
    if (c>=max):
        max=c
    a1 = a1 // 10
    i+=1
print 'Najveca cifra je=',max

