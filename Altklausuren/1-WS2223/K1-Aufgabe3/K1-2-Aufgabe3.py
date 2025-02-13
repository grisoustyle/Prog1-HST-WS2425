# Einbinden der Bibliothek 
import random 
 
# Erzeugt eine Zufallszahl im Intervall 1 <= zufallszahl <= 10 
counter = 0
score = "[_____]"
while counter <5:
    zufallszahl1 = random.randint(1, 10) 
    zufallszahl2 = random.randint(1,10)
    zufallsop = random.randint(1,2)
    if zufallsop == 1:
        operation = "+"
        ergebnis = zufallszahl1 + zufallszahl2
    else:
        operation = "-"
        ergebnis = zufallszahl1 - zufallszahl2

    antwort = int(input((f"{score} {zufallszahl1} {operation} {zufallszahl2}: ")))

    if antwort == ergebnis:
        counter +=1
        score = "["+(counter*"X")+((5-counter)*"_")+"]"
    else:
        print(f"richtig wäre {ergebnis} gewesen lmao")
print(f"{score} Gut gerechnet")