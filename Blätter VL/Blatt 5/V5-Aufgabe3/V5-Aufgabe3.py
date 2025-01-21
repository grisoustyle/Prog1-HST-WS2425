zahlA = float(input("A eingeben: "))
zahlB = float(input("B eingeben: "))

epsilon = 0.0001 #Genauigkeit
anzSchritte = 0

untergrenze = 0.0 #bzw 1.0
obergrenze = zahlA
#[0,a]

naherung = untergrenze + ((obergrenze-untergrenze)/2.0) #Mitte des aktuellen Bereichs

while abs(naherung * zahlB - zahlA) >= epsilon:
        print(f"unteres Limit: {untergrenze:.5f}, oberes Limit: {obergrenze:.5f}, aktuelle Näherung: {naherung:.5f}")
        
        anzSchritte += 1

        # Anpassung des Suchraums
        if naherung * zahlB < zahlA:  # Näherung ist zu klein
            untergrenze = naherung
            
        else:  # Näherung ist zu groß
            obergrenze = naherung

        # Neue Näherung berechnen
        naherung = untergrenze + (obergrenze - untergrenze) / 2.0

print(f"\nAnzahl Schritte: {anzSchritte}")
print(f"Angenähertes Ergebnis: {naherung:.5f}")
print(f"Prüfergebnis: {zahlA / zahlB:.5f}")