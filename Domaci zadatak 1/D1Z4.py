#Domaci rad: Vezba 1 zadatak 4
a=input("Unesite prvi broj: ")
b=input("Unesite drugi broj: ")
a1=float(a)
b1=float(b)
i=0
d=10.0
sumc=0
sum1=0
sum2=0
while i<4:
    sumc+=b1-(b1//d)*d
    if (i==0 or i==2):
        sum2+=a1-(a1//d)*d
    else:
        sum1+=a1-(a1//d)*d
    b1=b1//10
    a1=a1//10
    i+=1
print 'Suma cifara drugog broja=',sumc
print 'Razlika zbira cifara prvog broja na parnim i neparnim pozicijama',sum2-sum1
