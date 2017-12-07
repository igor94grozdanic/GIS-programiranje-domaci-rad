#Domaci rad: Vezba br. 2 zadatak 6
a=int(input("Unesi broj tacaka  "))
i=0
lista_x=[]
lista_y=[]
listak=[]
while i<a:
    x=raw_input("Unesite  koordinate X,Y  ")
    x1=x.split(",")
    lista_x.append(float(x1[0]))
    lista_y.append(float(x1[1]))
    i+=1
n=int(input("Unesi stepen polinoma  "))
i1=0
while i1<n:
    s=1
    t=1
    a1=1
    j=0
    while j<n:
        if j!=i1:
            s=s*(a1-lista_x[j])
            t=t*(lista_x[i1]-lista_y[j])
        j+=1
    listak.append((s/t)*lista_y[i1])
    i1+=1

print "Polinom P(X)=",round(listak[0],2),"*X^",n,
m=n
j1=1
while j1<len(listak):
    if listak[j1]>0:
        print "+",round(listak[j1],2),"*X^",m-1,
    else:
        print round(listak[j1],2), "*X^", m-1,
    j1+=1
    m-=1
print "+",a1