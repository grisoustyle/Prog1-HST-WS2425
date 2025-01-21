zahl = float(input("\nZahl eingeben: "))

def quadratwurzel_bin_alt(zahl):    
    epsilon = 0.01
    anzSchritte=0
    untergrenze = 1.0
    obergrenze = zahl
    naherung = untergrenze + ((obergrenze-untergrenze)/2.0)

    while abs(naherung**2-zahl)>=epsilon:
        print(f"Unteres Limit= {untergrenze}, Oberes Limit= {obergrenze}, Aktuelle Näherung= {naherung}")
        anzSchritte+=1
        if naherung**2<zahl:
            untergrenze = naherung
        else:
            obergrenze = naherung
        naherung = untergrenze + (obergrenze-untergrenze)/2.0

    print(f"Anzahl Schritte= {anzSchritte}")
    print(f"{naherung} ist unsere Näherung für die Quadratwurzel aus {zahl}")


def quadratwurzel_bin(zahl):
    epsilon = 0.001
    anzSchritte = 0

    if zahl >=1: 
        unteresLimit = 0.0
        oberesLimit = zahl
    else: 
        unteresLimit = zahl
        oberesLimit = 1.0

    naeherung = unteresLimit + (oberesLimit - unteresLimit) / 2.0

    while abs(naeherung**2 - zahl) >= epsilon:
        print(f"unteres Limit: {unteresLimit}, oberes Limit: {oberesLimit}, aktuelle Näherung: {naeherung}")
        
        anzSchritte += 1
        if naeherung**2 < zahl:
            unteresLimit = naeherung
        else:
            oberesLimit = naeherung
        naeherung = unteresLimit + (oberesLimit - unteresLimit) / 2.0

    print(f"\nAnzahl Schritte: {anzSchritte}")
    print(f"Angenähertes Ergebnis: {naeherung:.2f}")
    print(f"Prüfergebnis: {zahl**(1/2):.2f}")

def kubikwurzel_bin(zahl):
    epsilon = 0.001
    anzSchritte = 0

    if zahl >=1: 
        unteresLimit = 0.0
        oberesLimit = zahl
    else: 
        unteresLimit = zahl
        oberesLimit = 1.0

    naeherung = unteresLimit + (oberesLimit - unteresLimit) / 2.0

    while abs(naeherung**3 - zahl) >= epsilon:
        print(f"unteres Limit: {unteresLimit}, oberes Limit: {oberesLimit}, aktuelle Näherung: {naeherung}")
        
        anzSchritte += 1
        if naeherung**3 < zahl:
            unteresLimit = naeherung
        else:
            oberesLimit = naeherung
        naeherung = unteresLimit + (oberesLimit - unteresLimit) / 2.0

    print(f"\nAnzahl Schritte: {anzSchritte}")
    print(f"Angenähertes Ergebnis: {naeherung:.2f}")
    print(f"Prüfergebnis: {zahl**(1/3):.2f}")

quadratwurzel_bin(zahl)
kubikwurzel_bin(zahl)