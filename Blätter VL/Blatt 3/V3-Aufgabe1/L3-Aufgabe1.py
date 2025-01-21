"""
Übung 3.1
Schere, Stein, Papier

Wir wollen Schere, Stein, Papier spielen und dafür ein kleines Programm schreiben. 

Bitte denken Sie an folgende Punkte 
1)	Wenn der Nutzer eine fehlerhafte Eingabe macht, so wiederholen Sie die Einga-be bitte so lange, bis eine korrekte Eingabe erfolgt ist 
2)	So lange Computer und Nutzer unentschieden spielen soll das Spiel wiederholt werden 
3)	Beenden Sie das Spiel erst, wenn der Nutzer eine korrekte Eingabe gemacht hat und er entweder verloren oder gewonnen hat
"""

# bindet ein Modul ein – bitte Zeile ignorieren
import random

print("Lass uns Schere, Stein, Papier spielen!")

schereString = "Schere"
steinString = "Stein"
papierString = "Papier"

# optionen beinhaltet nun eine Liste mit den drei zulässigen Eingabe-Optionen
optionen = (schereString, steinString, papierString)

nutzerEingabe = input("Deine Eingabe (Schere, Stein, Papier): ")

while nutzerEingabe not in optionen:
    print("Fehlerhafte Eingabe!")
    nutzerEingabe = input("Deine Eingabe (Schere, Stein, Papier): ")

while nutzerEingabe in optionen:
    # random.choice(optionen) beinhaltet einen zufällig gewählten Eintrag aus optionen
    computerEingabe = random.choice(optionen)

    print("Deine Wahl: " + nutzerEingabe + "; Wahl des Computers: " + computerEingabe)

    if nutzerEingabe == computerEingabe:
        print("Unentschieden - neue Runde!")
        nutzerEingabe = input("Deine Eingabe (Schere, Stein, Papier): ")
        while nutzerEingabe not in optionen:
            print("Fehlerhafte Eingabe!")
            nutzerEingabe = input("Deine Eingabe (Schere, Stein, Papier): ")
    elif (
        (nutzerEingabe == steinString and computerEingabe == schereString)
        or (nutzerEingabe == papierString and computerEingabe == steinString)
        or (nutzerEingabe == schereString and computerEingabe == papierString)
    ):
        print("Du hast gewonnen!")
        break
    else:
        print("Du hast verloren!")
        break
