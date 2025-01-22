"""
Übung 4.3.2a
Dreiecke und Kreuze 

Schreiben Sie ein Programm, welches auf der Kommandozeile unter Angabe der Breite 
(zur Vereinfachung wieder nur ungerade Werte zulässig) ein Dreieck und ein Kreuz bestehend aus
Punkten (.) und Sternen (*) ausgibt: 
"""

# Nutzereingabe
breite = int(
    input("Maximale Breite des Dreiecks bzw. Kreuz als ungerade Zahl >3 eingeben: ")
)

# Prüfung der Eingabe
while not (breite > 3 and breite % 2 != 0):
    print("Die Eingabe war entweder nicht ungerade oder nicht >3")
    breite = int(input("Maximale Breite des Baums als ungerade Zahl >3 eingeben: "))

# Dreieck:
for anzahlPunkte in range(breite):
    print(anzahlPunkte * ". " + (breite - anzahlPunkte) * "* ")


print("\n\n -- \n\n")

sternzaehler = breite
for punktzaehler in range(breite):
    print(punktzaehler * ". " + sternzaehler * "* ")
    sternzaehler -= 1


"""
Übung 4.3.2b
Dreiecke und Kreuze 

Schreiben Sie ein Programm, welches auf der Kommandozeile unter Angabe der Breite 
(zur Vereinfachung wieder nur ungerade Werte zulässig) ein Dreieck und ein Kreuz bestehend aus
Punkten (.) und Sternen (*) ausgibt: 
"""

# Nutzereingabe
breite = int(
    input("Maximale Breite des Dreiecks bzw. Kreuz als ungerade Zahl >3 eingeben: ")
)

# Prüfung der Eingabe
while not (breite > 3 and breite % 2 != 0):
    print("Die Eingabe war entweder nicht ungerade oder nicht >3")
    breite = int(input("Maximale Breite des Baums als ungerade Zahl >3 eingeben: "))

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
