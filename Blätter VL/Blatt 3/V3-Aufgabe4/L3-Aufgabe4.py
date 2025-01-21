"""
Schreiben Sie folgende Programme. In allen Aufgaben ist n ein vom Benutzer angegeber Wert. 
1)	Geben Sie die Summe aller Zahlen von 1 bis n aus. Bestimmen Sie den Wert bitte, ohne die Gauß’sche Formel zu verwenden.
2)	Bestimmen Sie die Summe jeder n-ten Zahl zwischen 1 bis 100. 
3)	Geben Sie alle Primzahlen von 1 bis n aus. Bei der Bestimmung müssen Sie sich keine besondere Mühe bzgl. der Laufzeitkomplexität Ihrer Lösung geben. 
4)	Finden und benennen Sie alle natürlichen Zahlen zwischen 1 und 100, die durch n teilbar sind. n ist ein vom Benutzer angegebener Wert.
"""

# Nutzereingabe
n = int(input("Bitte Wert eingeben: "))

"""
1)	Geben Sie die Summe aller Zahlen von 1 bis n aus. Bestimmen Sie den Wert bitte, ohne die Gauß’sche Formel zu verwenden.
"""

sumValues = 0
for i in range(1, n + 1):
    sumValues += i

print("Summe der Werte von 1 bis " + str(n) + ": " + str(sumValues))

"""
2)	Bestimmen Sie die Summe jeder n-ten Zahl zwischen 1 bis 100. 
"""

sumValues = 0
for i in range(n, 100 + 1, n):
    sumValues += i

print("Summe jeder " + str(n) + "-ten Zahl zwischen 1 bis 100: " + str(sumValues))


"""
3)	Geben Sie alle Primzahlen von 1 bis n aus. Bei der Bestimmung müssen Sie sich keine besondere Mühe bzgl. der Laufzeitkomplexität Ihrer Lösung geben. 
"""

for i in range(n + 1):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
    if prime:
        print(i)

"""
4)	Finden und benennen Sie alle natürlichen Zahlen zwischen 1 und 100, die durch n teilbar sind. n ist ein vom Benutzer angegebener Wert.
"""
for i in range(1, 100):
    if i % n == 0:
        print(i)
