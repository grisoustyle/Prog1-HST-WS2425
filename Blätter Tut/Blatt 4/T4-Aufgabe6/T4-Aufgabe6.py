def ziffern_count(n):
    # Basisfall: Wenn n eine einstellige Zahl ist (0-9), haben wir die letzte Ziffer erreicht
    if n == 0:
        return 0
    else:
        # Rekursiver Aufruf: Zahl durch 10 teilen und 1 zur Ziffernanzahl hinzufügen
        return 1 + ziffern_count(n // 10)

# Eingabe
zahl = int(input("Geben Sie eine nicht-negative Zahl ein: "))

# Wenn die Zahl 0 ist, muss eine spezielle Behandlung erfolgen (sonst gibt die Funktion 0 zurück)
if zahl == 0:
    print(f"Die Anzahl der Ziffern in {zahl} ist: 1")
else:
    # Funktionsaufruf und Ausgabe
    anzahl_ziffern = ziffern_count(zahl)
    print(f"Die Anzahl der Ziffern in {zahl} ist: {anzahl_ziffern}")
