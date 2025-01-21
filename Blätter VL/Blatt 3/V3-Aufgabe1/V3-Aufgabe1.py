import random

print("Lass uns Schere, Stein, Papier spielen!")

schereString = "Schere"
steinString = "Stein"
papierString = "Papier"

# optionen beinhaltet nun eine Liste mit den drei zulässigen Eingabe-Optionen
optionen = (schereString, steinString, papierString)

# random.choice(optionen) beinhaltet einen zufällig gewählten Eintrag aus der Liste der Eingabe-Optionen
#computerEingabe = random.choice(optionen)

# Lassen Sie den Nutzer seine Wahl eingeben
#nutzerEingabe = str(input("Schere, Stein oder Papier? "))

gewonnen = False

# Prüfen Sie, ob die Nutzer-Eingabe zulässig ist
while not gewonnen:
    computerEingabe = random.choice(optionen)
    nutzerEingabe = str(input("Schere, Stein oder Papier? "))
    
    if nutzerEingabe not in optionen:
        print("Fehlerhafte Eingabe!")
        
    elif nutzerEingabe == computerEingabe:
        print("Unentschieden - neue Runde!") #Papier vs Papier, Schere vs Schere, Stein vs Stein

    elif nutzerEingabe == "Papier": #Papier vs ...
        if computerEingabe == "Schere": #Papier vs Schere
            print("Verloren!")
        else: #Papier vs Stein
            print("Gewonnen!")
            gewonnen = True

    elif nutzerEingabe == "Schere": #Schere vs ...
        if computerEingabe == "Stein": #Schere vs Stein
            print("Verloren!")
        else: #Schere vs Papier
            print("Gewonnen!")
            gewonnen = True

    else: #Stein vs ...
        if computerEingabe == "Schere": #Stein vs Papier
            print("Verloren!")
        else: #Stein vs Schere
            print("Gewonnen!")
            gewonnen = True