""" 
Übung 2.2
Tannenbäume auf der Kommandozeile

Sie möchten auf der Kommandozeile gerne einen vereinfachten Tannenbaum mit Sternchen malen. 
Hierfür darf der Nutzer die maximale Breite des Baums angeben. Die minimale Breite beträgt 5. 
Der Fuß des Baums hat immer die Höhe von einer Zeile und eine Breite von drei Zeichen. 
Zur Vereinfachung soll die Breite immer eine ungerade Zahl sein.
"""

# Nutzereingabe
breite = int(input("Maximale Breite des Baums als ungerade Zahl >3 eingeben: "))

# Prüfung der Eingabe
while not (breite > 3 and breite % 2 != 0):
    print("Die Eingabe war entweder nicht ungerade oder nicht >3")
    breite = int(input("Maximale Breite des Baums als ungerade Zahl >3 eingeben: "))

# linker Teil des Baums, abgerundet
linkeHaelfte = breite // 2

# Baum "wächst" Zeile für Zeile um 2 Sterne
for breiteBaumInZeile in range(1, breite + 1, 2):

    # Ausgabe: Leerzeichen links vom Baum
    # ergänzt um die eigentlichen Sterne für den Baum
    print(linkeHaelfte * " " + breiteBaumInZeile * "*")

    # Reduktion der linken Hälfte um 1
    linkeHaelfte -= 1

# Ausgabe des Fußes
print((breite // 2 - 1) * " " + "***")
