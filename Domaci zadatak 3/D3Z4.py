#Domaci rad: Vezba br. 3 zadatak 4

class Inzenjer:

    def __init__(self, ime="Pera", prezime="Peric", maticnibroj="00664", licenca="Nema licencu"):
        self._ime = ime
        self._prezime = prezime
        self._maticnibroj = maticnibroj
        self._licenca=licenca

    def dajIme(self):
        return self._ime

    def dajPrezime(self):
        return self._prezime

    def dajMaticnibroj(self):
        return self._maticnibroj

    def dajLicencu(self):
        return self._licenca

    def postaviIme(self,ime):
        self._ime = ime

    def postaviPrezime(self,prezime):
        self._prezime = prezime

    def postaviLicencu(self,licenca):
        self._licenca = licenca

    def postaviIme(self,maticnibroj):
        self._maticnibroj = maticnibroj

    def info(self):
        print self._ime,self._prezime,self._maticnibroj,self._licenca

class GeodetskiInzenjer(Inzenjer):

    def __init__(self, ime="Pera", prezime="Peric", maticnibroj="00664", licenca="Nema licencu",god_radni_staz=0):
        Inzenjer.__init__(self, ime, prezime,maticnibroj,licenca)
        self._god_radni_staz = god_radni_staz

    def dajGodStaz(self):
        return self._god_radni_staz

    def postaviGodStaz(self,godstaz):
        self._god_radni_staz = godstaz

    def infoLicenca(self):
        a=self.dajLicencu()
        if a=="Nema licencu":
            print "Inzenjer nema licencu"
        else:
            print "Licenca inzenjera je ",a

    def info(self):
        print self._ime,self._prezime,self._maticnibroj,self._licenca,self._god_radni_staz

class ElektrotehnickiInzenjer(Inzenjer):

    def __init__(self, ime="Pera", prezime="Peric", maticnibroj="00664", licenca="Nema licencu", br_projekata=0):
        Inzenjer.__init__(self, ime, prezime, maticnibroj, licenca)
        self._br_projekata = br_projekata

    def dajBrProjekata(self):
        return self._br_projekata

    def postaviBrProjekata(self, br_projekata):
        self._br_projekata = br_projekata

    def infoLicenca(self):
        a = self.dajLicencu()
        if a == "Nema licencu":
            print "Inzenjer nema licencu"
        else:
            print "Licenca inzenjera je ",a

    def info(self):
        print self._ime, self._prezime, self._maticnibroj, self._licenca, self._br_projekata

#Glavni program

ime=raw_input("Unesite ime inzenjera  ")
prezime=raw_input("Unesite prezime inzenjera  ")
matic=raw_input("Unesite maticni broj inzenjera  ")
lic=raw_input("Unesite licencu inzenjera  ")
god=int(input("Unesite broj projekata  "))
a=ElektrotehnickiInzenjer(ime,prezime,matic,lic,god)
a.info()
print a.dajIme()
#a.postaviLicencu("Nema licencu")
a.infoLicenca()
a.info()