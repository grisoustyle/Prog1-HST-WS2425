#A2
preis = 0.5
menge=int(input("Bestellte Menge: "))
if menge <=0:
    print(0)
elif menge <100:
    print("Kunde muss Zahlen: ",menge*preis,"€")
elif menge <500:
    print("Kunde muss Zahlen: ",menge*preis*(1-0.03),"€")
elif menge <1000:
    print("Kunde muss Zahlen: ",menge*preis*(1-0.05),"€")
elif menge >=1000:
    print("Kunde muss Zahlen: ",menge*preis*(1-0.07),"€")
else:
    print("Fehler")