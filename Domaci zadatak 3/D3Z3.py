#Domaci rad: Vezba br. 3 zadatak 3
import math

#Klasa Povrs
class Tacka:

    def __init__(self, x = 0, y = 0, z=0, ID=0):
        self.x = x
        self.y = y
        self.z = z
        self.ID=ID

    def rastojanjeDo(self,t):
        dx=(self.x-t.x)**2
        dy = (self.y - t.y)**2
        return math.sqrt(dx+dy)

    def veceZ(self,t):
        if self.z >= t.z:
            return self
        else:
            return t

    def manjeZ(self, t):
        if self.z <= t.z:
            return self
        else:
            return t

    def str(self):
        print  self.x ,self.y, self.z, self.ID


class Povrs:

    def __init__(self,ime,lista_tacaka,broj_tacaka):
        self.ime = ime
        self.lista_tacaka =lista_tacaka
        self.broj_tacaka=broj_tacaka

    def metaPodaci(self):
        for i in self.lista_tacaka:
            i.str()
        print  "Ime osobe koja analizira povrs: ",self.ime
        print "Broj tacaka povrsi: ",self.broj_tacaka

    def najblizaTacka(self,t):
        najbl=99999999999
        tacka=Tacka()
        for i in lista_tacaka:
            if i.ID!=t.ID:
                if t.rastojanjeDo(i)<najbl:
                    najbl=t.rastojanjeDo(i)
                    tacka=i
        return tacka.ID

    def srednjaPovrs(self):
        listax=[]
        listay=[]
        for j1 in self.lista_tacaka:
            listax.append(float(j1.x))
            listay.append(float(j1.y))
        xp1=[]
        xp1.append(float(listax[int(len(listax))-1]))
        xp2=[]
        i=0
        while i<int((len(listax)-1)):
            xp1.append(float(listax[i]))
            i+=1
            xp2.append(float(listax[i]))
        xp2.append(float(listax[0]))
        j=0
        sum=0
        while j<len(listax):
            sum+=listay[j]*(xp1[j]-xp2[j])
            j+=1
        re=[listay,xp1,xp2]
        sum1=float(sum)
        pov=sum1*0.5
        return pov

    def mini(self,lista):
        i=0
        mine=9999999999999999999999
        while i<len(lista):
            if (lista[i]<mine):
                mine=lista[i]
            i+=1
        return mine

    def maxi(self,lista):
        i = 0
        maxe =-99999999999999999
        while i < len(lista):
            if (lista[i] > maxe):
                maxe = lista[i]
            i += 1
        return maxe

    def MBBOX(self):
        listax = []
        listay = []
        for j1 in self.lista_tacaka:
            listax.append(float(j1.x))
            listay.append(float(j1.y))
        return [(self.mini(listax),self.maxi(listay)),(self.maxi(listax),self.maxi(listay)),(self.maxi(listax),self.mini(listay)),(self.mini(listax),self.mini(listay))]

    def vratiTacku(self,id):
        i=0
        d=len(self.lista_tacaka)
        while i<d:
            if lista_tacaka[i].ID==id:
                return lista_tacaka[i]
                i=i+d
            i+=1

    def interpolacija(self,i1,i2,t):
        a=self.vratiTacku(i1)
        b=self.vratiTacku(i2)
        if ((a.rastojanjeDo(t)+b.rastojanjeDo(t))==a.rastojanjeDo(b)):
            veca=a.veceZ(b)
            manja=a.manjeZ(b)
            x1=veca.z-manja.z
            d1=veca.rastojanjeDo(t)
            d=veca.rastojanjeDo(manja)
            x=(x1*d1)/d
            t.z=veca.z-x
            return t
        else:
            t.z="Tacka za interpolaciju nije na pravcu."
            return t
#Glavni program
n=int(input("Unesite broj tacaka  "))
i=0
lista_tacaka=[]
lista_id=[]
while i<n:
    x=raw_input("Unesite koordinate (nacin unosa je x,y,z) ")
    c=x.split(",")
    id=input("Unesite ID tacke  ")
    if lista_id.count(id)!= 0:
        print "Vec postoji taj ID molimo unesite drugi"
        id=id=input("Unesite ID tacke  ")
    lista_id.append(id)
    lista_tacaka.append(Tacka((float(c[0])),(float(c[1])),(float(c[2])),id))
    i+=1
ime=raw_input("Unesite ime operatera  ")
p=Povrs(ime,lista_tacaka,int(n))
a=Tacka()
a1=p.najblizaTacka(a)
print "Najbliza tacki a je tacka sa sledecim ID-ijem  ",a1
l=p.srednjaPovrs()
print "Srednja povrsina je=  ",l
print "Koordinate minimalnog obuhvatnog pravougaonika su (x,y)  ",p.MBBOX()
x1=raw_input("Unesite koordinate tacke koju zelite da interpolujete (nacin unosa je x,y) ")
c1=x1.split(",")
ti=Tacka((float(c1[0])),(float(c1[1])),0)
id1=input("Unesite ID prve tacke koja ucestvuje u interpolaciji ")
id2=input("Unesite ID druge tacke koja ucestvuje u interpolaciji ")
inter=p.interpolacija(id1,id2,ti).z
print "Interpolovana visina za trazenu tacku je  ",inter


