def pascal(z, s):
    if s == 1 or s == z:
        return 1
    else:
        return pascal(z - 1, s - 1) + pascal(z - 1, s)

def pascal_dreieck(hoehe):
    for z in range(1, hoehe + 1):
        # Leerzeichen für Zentrierung
        leerzeichen = " " * (hoehe - z)
        # Erzeuge eine Zeile mit den Pascal-Werten
        zeile = [str(pascal(z, s)) for s in range(1, z + 1)]
        print(leerzeichen + " ".join(zeile))

hoehe = int(input("Geben Sie die Höhe des Pascal-Dreiecks ein: "))
pascal_dreieck(hoehe)
