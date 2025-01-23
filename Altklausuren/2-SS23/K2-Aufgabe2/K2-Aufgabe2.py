def ist_prime(zahl):
    """Überprüft, ob eine Zahl eine Primzahl ist."""
    if zahl < 2:
        return False
    for i in range(2, int(zahl ** 0.5) + 1):
        if zahl % i == 0:
            return False
    return True

def produkt_der_primzahlen(n):
    """Berechnet das Produkt der ersten n Primzahlen."""
    primzahlen = []
    zahl = 2
    produkt = 1
    count = 1
    
    while len(primzahlen) < n:
        if ist_prime(zahl):
            primzahlen.append(zahl)
            print(f"Primzahl {count}: {zahl}")
            produkt *= zahl
            count += 1
        zahl += 1
    
    print(f"\nProdukt der ersten {n} Primzahlen: {produkt}")

# Benutzerabfrage
n = int(input("Geben Sie die Anzahl der Primzahlen ein, deren Produkt berechnet werden soll: "))
produkt_der_primzahlen(n)
