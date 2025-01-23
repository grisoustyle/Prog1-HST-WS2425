# Einbinden der Bibliothek 
import random 
 
def rechentrainer():
    korrekt = 0
    progressbar = "[_____]"
    while korrekt <5:
        zahl1 = random.randint(1,10)
        zahl2 = random.randint(1,10)
        symbol = random.randint(1,2)

        if symbol == 1: #+
            richtiges_ergebnis = zahl1 + zahl2
            antwort = int(input(f"{progressbar} {zahl1} + {zahl2} = "))
        else: #-
            richtiges_ergebnis = zahl1 - zahl2
            antwort = int(input(f"{progressbar} {zahl1} - {zahl2} = "))

        if antwort == richtiges_ergebnis:
            korrekt +=1
            progressbar = "[" + korrekt*"X" + (5-korrekt)*"_"+ "]"
        else:
            print(f"Falsch, korrekte Antwort wäre {richtiges_ergebnis}")
    if korrekt == 5:
        print(f"{progressbar} Gut gerechnet!")
        

rechentrainer()