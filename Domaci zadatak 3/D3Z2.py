#Domaci rad: Vezba br. 3 zadatak 2
import math
#Klasa Tacka
class Tacka:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def pomeri(self,x_pomeraj,y_pomeraj):
        self.x=self.x+x_pomeraj
        self.y = self.y + y_pomeraj

    def rastojanjeDo(self,t):
        dx=(self.x-t.x)**2
        dy = (self.y - t.y)**2
        return math.sqrt(dx+dy)
#Klasa Duz
class Duz:

    def __init__(self,p=0,k=0):
        self.p=p
        self.k=k

    def kreiraj_duz(self,xp,yp,xk,yk):
        p=Tacka(xp,yp)
        k=Tacka(xk,yk)
        d=Duz(p,k)
        return d

    def duzinaDuzi(self):
        return self.p.rastojanjeDo(self.k)
    def str(self):
        print self.p.x,self.p.y,self.k.x,self.k.y,

# Glavni program
xp=float(input("Unesite x koordinatu pocetne tacke"))
yp=float(input("Unesite y koordinatu pocetne tacke"))
xk=float(input("Unesite x koordinatu krajnje tacke"))
yk=float(input("Unesite y koordinatu krajnje tacke"))
p=Tacka(xp,yp)
k=Tacka(xk,yk)
druga_duz=Duz(k,p)
druga_duz1=druga_duz.kreiraj_duz(10,12,15,16)
prva_duz=Duz(p,k)
print "Prva duz je sa sledecim koordinatama (x_pocetni,y_pocetni,x_krajnji,y_krajnji) " ,prva_duz.str()
print "Druga duz je sa sledecim koordinatama(x_pocetni,y_pocetni,x_krajnji,y_krajnji)",druga_duz1.str()
dx=float(input("Unesite dx"))
dy=float(input("Unesite dy"))
k.pomeri(dx,dy)
nova_duz=Duz(p,k)
print "Nova duz (x_pocetni,y_pocetni,x_krajnji,y_krajnji) ", nova_duz.str()

