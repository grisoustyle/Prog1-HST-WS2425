#Dreiecke und Kreuze
breite = int(input("Breite: "))
breitep=0

#Dreieck
if breite%2==0:
    print("Unzulässige Breite")
else:

    for i in range(breite):
        print((breitep+i)*". " + "* "*(breite-i))


# Prüfung der Eingabe
while not (breite > 3 and breite % 2 != 0):
    print("Die Eingabe war entweder nicht ungerade oder nicht >3")
    breite = int(input("Maximale Breite des Baums als ungerade Zahl >3 eingeben: "))

print("\n")
# Kreuz:
distanzAnfangEnde = 0
for zeilenPos in range(breite):
    zeilenString = ""
    for lininenPos in range(breite):
        if (
            lininenPos == distanzAnfangEnde
            or (breite - lininenPos - 1) == distanzAnfangEnde
        ):
            zeilenString += "* "
        else:
            zeilenString += ". "
    distanzAnfangEnde += 1
    print(zeilenString)