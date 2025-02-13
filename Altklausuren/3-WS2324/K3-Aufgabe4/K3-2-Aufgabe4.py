def zahlenpyramide(hoehe):
    zahl = 0  # Startwert der Zahlenfolge
    for i in range(1, hoehe + 1):
        # Erzeuge Leerzeichen für die Zentrierung
        leerzeichen = " " * (hoehe - i)
        # Erzeuge die Zahlenreihe für die aktuelle Zeile
        zeile = [str(zahl % 10) for zahl in range(zahl, zahl + i)]
        zahl += i  # Update für die nächste Zeile
        print(leerzeichen + " ".join(zeile))  # Ausgabe der Zeile mit Leerzeichen

hoehe = int(input("Geben Sie die Höhe der Pyramide ein: "))
zahlenpyramide(hoehe)