testliste = [
    "Apfel",
    "Banane",
    "Hund",
    42,
    9.12
]
###############

print(f"{testliste}\n")

###############

for items in testliste:
    print(f"{items}: {type(items)}")
   
###############

testliste[0]="Birne"

###############

testliste.append(34.56)

###############

zahlenliste = [
    4.58,
    49,
    7,
    2.5,
    4.8,
    99,
    123
]
print(f"\n{zahlenliste}")
print(f"{testliste}\n")

###############

neue_liste=[]
for item_t in testliste:
    if type(item_t) == int or type(item_t) == float:
        
        for item_z in zahlenliste:
            item_t = item_t + item_z
    
        neue_liste.append(item_t)

print(f"Zahlenaddierte Liste: {neue_liste}\n")

###############

def zahlenadder(liste,start,ende):
    if start <= ende:
        return liste[start]+ (zahlenadder(liste,start+1,ende))
    else:
        return 0
    
print(f"Ersten 5 addiert: {zahlenadder(zahlenliste,0,4)}")
print(f"Mittlere 5 addiert: {zahlenadder(zahlenliste,1,5)}")
print(f"Letzte 5 addiert: {zahlenadder(zahlenliste,2,6)}")

###############

print(f"\nCheck ob Banane enthalten: {('Banane' in testliste)}")

###############

zahlenliste[1] = "49"
print(f"\nGeänderte 49: {zahlenliste}")

###############

summe = 0
for item in zahlenliste:
    #summe += item geht nicht weil int + str
    summe += float(item)
print(f"\nSumme aller Zahlen: {summe}")