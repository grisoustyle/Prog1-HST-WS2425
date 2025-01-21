def kubikwurzel_bin(zahl):
    epsilon = 0.01
    anzSchritte=0
    untergrenze = 1.0
    obergrenze = zahl
    naherung = untergrenze + ((obergrenze-untergrenze)/2.0)

    while abs(naherung**3-zahl)>=epsilon:
        print(f"Unteres Limit= {untergrenze}, Oberes Limit= {obergrenze}, Aktuelle Näherung= {naherung}")
        anzSchritte+=1
        if naherung**3<zahl:
            untergrenze = naherung
        else:
            obergrenze = naherung
        naherung = untergrenze + (obergrenze-untergrenze)/2.0

    print(f"Anzahl Schritte= {anzSchritte}")
    print(f"{naherung} ist unsere Näherung für die Kubikwurzel aus {zahl}")