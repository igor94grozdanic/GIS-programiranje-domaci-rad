#Domaci rad: Vezba br. 3 zadatak 5

class Osoba:

    def __init__(self, ime="Pera", prezime="Peric", datum_rodjenja="01.01.1990.", adresa="Njegoseva 15"):
        self._ime = ime
        self._prezime = prezime
        self._datum_rodjenja = datum_rodjenja
        self._adresa=adresa

    def dajIme(self):
        return self._ime

    def dajPrezime(self):
        return self._prezime

    def dajDatumRodjenja(self):
        return self._datum_rodjenja

    def dajAdresu(self):
        return self._adresa

    def postaviIme(self,ime):
        self._ime = ime

    def postaviPrezime(self,prezime):
        self._prezime = prezime

    def postaviAdresu(self,adresa):
        self._adresa = adresa

    def postaviDatumRodjenja(self,datum_rodjenja):
        self._datum_rodjenja = datum_rodjenja

    def info(self):
        print self._ime,self._prezime,self._datum_rodjenja,self._adresa

class Djak(Osoba):

    def __init__(self, ime="Pera", prezime="Peric", datum_rodjenja="01.01.1990.", adresa="Njegoseva 15",naziv_skole="Sveti Sava",odeljenje="II-2",godina_upisa="2017"):
        Osoba.__init__(self, ime, prezime,datum_rodjenja,adresa)
        self._naziv_skole = naziv_skole
        self._odeljenje = odeljenje
        self._godina_upisa = godina_upisa

    def dajNazivSkole(self):
        return self._naziv_skole

    def dajOdeljenje(self):
        return self._odeljenje

    def dajGodinuUpisa(self):
        return self._godina_upisa

    def postaviNazivSkole(self,naziv_skole):
        self._naziv_skole = naziv_skole

    def postaviOdeljenje(self,odeljenje):
        self._odeljenje = odeljenje

    def postaviGodinuUpisa(self,godina_upisa):
        self._godina_upisa = godina_upisa

    def trenutniRazred(self):
        a=str(self.dajOdeljenje())
        a1=a.split("-")
        return a1[0]

    def obnavljanje(self,p):
        l=self.dajDatumRodjenja()
        l1=l.split(".")
        godr=int(l1[2])
        u=int(self.dajGodinuUpisa())
        brgod=2017-godr
        if p==brgod:
           print "Nije ponavljao"
        else:
            print "Ponavljao je"


    def info(self):
        print self._ime,self._prezime,self._datum_rodjenja,self._adresa,self._naziv_skole,self._odeljenje,self._godina_upisa

class Zaposlen(Osoba):

    def __init__(self, ime="Pera", prezime="Peric", datum_rodjenja="01.01.1990.", adresa="Njegoseva 15",kompanija="RGZ",departman="II",lista_zakljucenja=[],lista_prekida=[]):
        Osoba.__init__(self, ime, prezime,datum_rodjenja,adresa)
        self._kompanija = kompanija
        self._departman = departman
        self._lista_zakljucenja = lista_zakljucenja
        self._lista_prekida = lista_prekida

    def dajKompaniju(self):
        return self._kompanija

    def dajDepartman(self):
        return self._departman

    def dajListuZakljucenja(self):
        return self._lista_zakljucenja

    def dajListuPrekida(self):
        return self._lista_prekida

    def postaviKompaniju(self,kompanija):
        self._kompanija = kompanija

    def postaviDepartman(self,departman):
        self._departman = departman

    def postaviListuZakljucenja(self,lista_zakljucenja):
        self._lista_zakljucenja = lista_zakljucenja

    def postaviListuPrekida(self,lista_prekida):
        self._lista_prekida = lista_prekida

    def radniStaz(self):
        listaz=self.dajListuZakljucenja()
        listap=self.dajListuPrekida()
        i=0
        brrd=0
        while i<len(listap):
            z=listaz[i]
            p=listap[i]
            z1=z.split(".")
            p1=p.split(".")
            d1=int(z1[0])
            m1=int(z1[1])
            g1 = int(z1[2])
            d2 = int(p1[0])
            m2 = int(p1[1])
            g2 = int(p1[2])
            if d1<=d2:
                d=d2-d1
            else:
                d=d2-d1+30
                m2=m2-1
            if m1 <= m2:
                 m=m2-m1
            else:
                m=m2-m1+12
                g2=g2-1
            g=g2-g1
            brm=m+g*12
            brrd=brrd+brm*30+d
            i+=1
        return brrd

    def info(self):
        print self._ime,self._prezime,self._datum_rodjenja,self._adresa,self._kompanija,self._departman,self._lista_zakljucenja,self._lista_prekida

#Glavni program
recnik1 = {'Prvi razred':7, 8:'Drugi razred', 9:'Treci razred' , 10:'Cetvrti razred',11:'Peti razred',12: 'Sesti razred',13:'Sedmi razred', 14:'Osmi razred'}
recnik2 = {'I':'Prvi razred', 'II':'Drugi razred', 'III':'Treci razred' , 'IV':'Cetvrti razred','V':'Peti razred','VI': 'Sesti razred','VII':'Sedmi razred', 'VIII':'Osmi razred'}
kontr=raw_input("Unesite oznaku za koju vrstu osobe hocete da unosite podatke (D-djak, Z-zaposlen)  ")
if kontr=="D":
    ime = raw_input("Unesite ime djaka  ")
    prezime = raw_input("Unesite prezime djaka  ")
    datumr = raw_input("Unesite datum rodjenja djaka (dan.mesec.godina)  ")
    adresa = raw_input("Unesite adresu djaka  ")
    skola = raw_input("Unesite naziv skole u koju djak ide  ")
    odeljenje = raw_input("Unesite odeljenje u koje djak trenutno ide (razred - odeljenje (npr. I-1, II-2, III-3....)  " )
    datumup = raw_input("Unesite godinu upisa  ")
    dj=Djak(ime,prezime,datumr,adresa,skola,odeljenje,datumup)
    r=dj.trenutniRazred()
    print "Djak trenutno ide u  ",recnik2[r]
    dj.obnavljanje(recnik1[recnik2[r]])
    dj.info()

elif kontr=="Z":
    lista_z=[]
    lista_p=[]
    ime = raw_input("Unesite ime zaposlenog  ")
    prezime = raw_input("Unesite prezime zaposlenog  ")
    datumr = raw_input("Unesite datum rodjenja zaposlenog (dan.mesec.godina)  ")
    adresa = raw_input("Unesite adresu zaposlenog  ")
    kompanija = raw_input("Unesite naziv kompanije  ")
    departman = raw_input("Unesite naziv departmana  ")
    brf=int(input("Unesite broj firmi u kojima je zaposlen do sada radio.  "))
    i=0
    while i<brf:
        datum_zakljucenja = raw_input("Unesite datum zakljucenja radnog odnosa (dan.mesec.godina: 12.2.2008)  ")
        datum_prekida = raw_input("Unesite datum prekida radnog odnosa (dan.mesec.godina: 13.8.2010)  ")
        lista_z.append(datum_zakljucenja)
        lista_p.append(datum_prekida)
        i+=1
    nr=raw_input("Da li zaposlen trenutno negde radi(DA ili NE)  ")
    if nr=="DA":
        datum_zakljucenja=raw_input("Unesite datum zakljucenja novog ugovora (dan.mesec.godina: 12.2.2008)  ")
        datum_prekida = raw_input("Unesite danasnji datum (dan.mesec.godina: 12.8.2018)  ")
        lista_z.append(datum_zakljucenja)
        lista_p.append(datum_prekida)
    za = Zaposlen(ime, prezime, datumr, adresa, kompanija, departman, lista_z,lista_p)
    lis=[za.radniStaz()/30,za.radniStaz()%30]
    print "Radni staz zaposlenog je tacno ",lis[0] , " meseci i ", lis[1], "dana."
    za.info()
else:
    print "Pogresno ste uneli oznaku za vrstu osobe"