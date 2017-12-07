#Domaci rad: Vezba br. 3 zadatak 1
import math
#Klasa sfera
class Sfera:
    broj=0
    def __init__(self, x = 0, y = 0,z=0,r=1):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        Sfera.broj += 1

    @staticmethod
    def broj_sfera():
        return (Sfera.broj)

    def zapremina(self):
        v=float(self.r)
        return (4/3)*v**3*math.pi

# Glavni program

print Sfera.broj_sfera()
sfera=Sfera(0,0,0,4.0)
globus=Sfera(1.0,1.0,1.0,12)
bilijarska_lopta=Sfera(10.0,10.0,10.0,10.0)
jedinicna_sfera=Sfera()
print Sfera.broj_sfera()
print "Zapremina sfere je", sfera.zapremina()
print "Zapremina globusa je", globus.zapremina()
print "Zapremina bilijarske_lopte je", bilijarska_lopta.zapremina()
print "Zapremina jedinicne_sfere je", jedinicna_sfera.zapremina()



