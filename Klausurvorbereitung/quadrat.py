#_______
#_XXXXX_
#_X___X_
#_X_X_X_
#_X___X_
#_XXXXX_
#_______

def alternierendes_quadrat(breite):
    for y in range(breite):
        for x in range(breite):
            # Abstand zum nächsten Rand
            abstand = min(x, y, breite - x - 1, breite - y - 1)
            # Wechsel zwischen '_' und 'X' je nach Parität des Abstands
            print('X' if abstand % 2 else ' ', end='')
        print()  # Neue Zeile nach jeder Zeile

# Beispiel
alternierendes_quadrat(11)