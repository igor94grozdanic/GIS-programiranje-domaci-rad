#Domaci rad: Vezba 1 zadatak 3
p1=raw_input("Unsite prvi pravac (stepeni:minuti:sekunde) ")
p2=raw_input("Unsite drugi pravac (stepeni:minuti:sekunde) ")
pp=p1.split(":")
as1=int(pp[0])
am=int(pp[1])
ase=int(pp[2])
dp=p2.split(":")
bs=int(dp[0])
bm=int(dp[1])
bse=int(dp[2])

if(am<60 and ase<60 and bm<60 and bse<60):
    a=float(as1)+float(am)/60+float(ase)/3600
    b=float(bs)+float(bm)/60+float(bse)/3600
else:
    print 'greska pri unosu'

if(a<=b):
    razlika=b-a
else:
    razlika=360-(a-b)
razlika1=round(razlika,4)
print'Ugao izmedju dva zadata pravca je= ',razlika1


