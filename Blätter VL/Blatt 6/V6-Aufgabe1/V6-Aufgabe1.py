
# 3/k=x
# x^3=k

# f(x)= x^3-k
# f'(x)= 3x^2

def newton_kubikwurzel(zahl):
    #Abbruchkriterium
    episilon = 0.01

    #Initiale Schätzung
    schaetzung = zahl/3

    #Zähler
    durchlauf = 0

    while abs(schaetzung**3 - zahl) >= episilon:
        schaetzung = schaetzung - ((schaetzung**3)-zahl) / (3*(schaetzung**2)) #x0 -   f(schätzung) / f'(schätzung)
        durchlauf +=1
        print(f"Durchlauf {durchlauf}, Näherung {schaetzung}")
    print("-"*10+ f"\nKubikwurzel aus {zahl} ist näherungsweise {schaetzung}.\nAnzahl Durchläufe: {durchlauf}\n")

    return schaetzung,durchlauf

#newton_kubikwurzel(int(input("Zahl eingeben: ")))

def bin_kubikwurzel(zahl):
    #Abbruchkriterium
    epsilon = 0.01

    #Grenzen
    unteresLimit = 0 
    oberesLimit = zahl

    #Schätzung
    schaetzung = unteresLimit + (oberesLimit - unteresLimit)/2.0
    
    #Zähler
    durchlauf = 0

    while abs(schaetzung**3-zahl) >= epsilon:
        if schaetzung**3 < zahl:
            unteresLimit = schaetzung
        else:
            oberesLimit = schaetzung
        durchlauf +=1
        print(f"Durchlauf {durchlauf}, Näherung {schaetzung}")

        schaetzung = unteresLimit + (oberesLimit - unteresLimit)/2.0
    print("-"*10+f"\nKubikwurzel aus {zahl} ist näherungsweise {schaetzung}.\nAnzahl Durchläufe: {durchlauf}\n")
    return schaetzung,durchlauf




wahl = int(input("Verfahren wählen.\n'1' für Binär,\n'2' für Newton,\n'3' für einen Vergleich\n"))
if wahl ==1:
    bin_kubikwurzel(int(input("\nZahl eingeben: ")))
elif wahl ==2:
    newton_kubikwurzel(int(input("\nZahl eingeben: ")))
elif wahl ==3:
    zahl = int(input("\nZahl eingeben: "))
    print (f"\nKubikwurzel aus {zahl} mithilfe Binärer Suche:")
    bin_schaetzung, bin_durchlauf = bin_kubikwurzel(zahl)
    print (f"\nKubikwurzel aus {zahl} mithilfe Newton Verfahren:")
    newton_schaetzung, newton_durchlauf = newton_kubikwurzel(zahl)
    print("\n"+"="*10)
    print (f"Eingabewert: {zahl}\nBinär-Schätzung: {bin_schaetzung} mit {bin_durchlauf} Durchläufen.")
    print (f"\nNewton-Schätzung: {newton_schaetzung} mit {newton_durchlauf} Durchläufen.\n")
