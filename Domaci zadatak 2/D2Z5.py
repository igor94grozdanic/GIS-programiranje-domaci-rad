#Domaci rad: Vezba br. 2 zadatak 5
recenica=raw_input("Unesite vasu recenicu  ")
i=0
s=len(recenica)
while i<s:
    if recenica[i]==" ":
        i+=1
    else:
        print recenica[i]
        i+=1

