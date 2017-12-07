#Domaci rad: Vezba 1 zadatak 7
pt=raw_input("Unesite koordinate za tacku A (x,y):  ")
ptt=pt.split(",")
a=float(ptt[0])
b=float(ptt[1])
pt1=raw_input("Unesite koordinate za tacku B (x,y):  ")
ptt1=pt1.split(",")
a1=float(ptt1[0])
b1=float(ptt1[1])
pt2=raw_input("Unesite koordinate za tacku C (x,y):  ")
ptt2=pt2.split(",")
a2=float(ptt2[0])
b2=float(ptt2[1])
pt3=raw_input("Unesite koordinate za tacku M (x,y):  ")
ptt3=pt3.split(",")
a3=float(ptt3[0])
b3=float(ptt3[1])
def ptr( x1,y1,x2,y2,x3,y3 ):
    a=x1*(y2-y3)
    b=x2*(y3-y1)
    c=x3*(y1-y2)
    p=abs((a+b+c)/2)
    return p
p1=ptr(a,b,a1,b1,a3,b3)
p2=ptr(a1,b1,a2,b2,a3,b3)
p3=ptr(a,b,a2,b2,a3,b3)
n=p1+p2+p3
s=ptr(a,b,a1,b1,a2,b2)
if (n==s):
    print 'Tacka M upada u tougao ABC.'
else:
    print 'Tacka M ne upada u tougao ABC.'


