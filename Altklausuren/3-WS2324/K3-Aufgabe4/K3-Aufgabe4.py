hoehe = int(input("Höhe "))
'''#3
schicht = 1

0
schicht +1
1 2
schicht +1
3 4 5'''

# Zahlenpyramide erstellen
aktuelle_zahl = 0  # Startwert für die Zahlen
for zeile in range(1, hoehe + 1):  # Zeilen steuern
    for spalte in range(zeile):  # Spalten in jeder Zeile steuern
        print(aktuelle_zahl % 10, end=" ")  # Zahl ausgeben, von 0 bis 9
        aktuelle_zahl += 1  # Zahl erhöhen
    print()  # Zeilenumbruch nach jeder Zeile
