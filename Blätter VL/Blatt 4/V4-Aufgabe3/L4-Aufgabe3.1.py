""" 
Übung 3.1

Häuser auf der Kommandozeile

Sie möchten auf der Kommandozeile gerne vereinfachte Häuser malen. 
Hierfür darf der Nutzer die maximale Breite des Hauses angeben und die Höhe des Baukörpers. 
Die minimale Breite beträgt 5 und die minimale Höhe 3. Das Haus hat im linken Teil immer eine 
Tür der Höhe 2. Zur Vereinfachung soll die Breite immer eine ungerade Zahl sein.
"""

# Nutzereingabe
breite = int(input("Maximale Breite des Baums als ungerade Zahl >3 eingeben: "))

# Prüfung der Eingabe
while not (breite > 3 and breite % 2 != 0):
    print("Die Eingabe war entweder nicht ungerade oder nicht >3")
    breite = int(input("Maximale Breite des Baums als ungerade Zahl >3 eingeben: "))

hoehe = int(input("Höhe des Baukörpers als Zahl >=3 eingeben: "))
# Prüfung der Eingabe
while not (hoehe >= 3):
    print("Die Eingabe ist nicht >= 3")
    hoehe = int(input("Höhe des Baukörpers als Zahl >=3 eingeben: "))

# linker Teil des Baums, abgerundet
linkeHaelfte = breite // 2

# Dach "wächst" Zeile für Zeile um 2 Sterne
for breiteBaumInZeile in range(1, breite + 1, 2):
    
    #print("breiteBaumInZeile: " + str(breiteBaumInZeile))

    # Ausgabe: Leerzeichen links vom Baum
    # ergänzt um die eigentlichen Sterne für den Baum
    print(linkeHaelfte * " " + breiteBaumInZeile * "*")

    # Reduktion der linken Hälfte um 1
    linkeHaelfte -= 1

# Ausgabe des Baukörpers
hoehenZaehler = hoehe-1
while hoehenZaehler >0:
    if (hoehenZaehler>2):
        print (breite * "*")
    else:
        print ("*  " + (breite-3)*"*")
    hoehenZaehler -= 1

