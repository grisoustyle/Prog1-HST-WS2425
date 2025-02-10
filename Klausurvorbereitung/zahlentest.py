#46750583
#46.750.583


def format_number(zahl):
    neue_zahl = []
    
    while zahl > 0:
        neue_zahl.append(str(zahl % 1000))
        zahl //= 1000  # Zahl um drei Stellen kürzen
        print(neue_zahl)
    
    return ".".join(neue_zahl[::-1])  # Reihenfolge umdrehen und mit Punkten verbinden

# Test
zahl = 46750583
print(format_number(zahl))  # Ausgabe: 46.750.583

