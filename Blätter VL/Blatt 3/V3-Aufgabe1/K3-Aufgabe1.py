# bindet ein Modul ein – bitte Zeile ignorieren 
import random 
 
print("Lass uns Schere, Stein, Papier spielen!") 
 
schereString = "Schere" 
steinString = "Stein" 
papierString = "Papier" 
 
# optionen beinhaltet nun eine Liste mit den drei zulässigen Eingabe-Optionen 
optionen = (schereString, steinString, papierString) 
 
# random.choice(optionen) beinhaltet einen zufällig gewählten Eintrag aus der Liste der Eingabe-Optionen 
 
# Lassen Sie den Nutzer seine Wahl eingeben 
 
# Prüfen Sie, ob die Nutzer-Eingabe zulässig ist 
gewonnen = False
while not gewonnen:
    computerEingabe = random.choice(optionen) 

    nutzerEingabe = str(input("Deine Eingabe (Schere, Stein, Papier): "))

    if nutzerEingabe not in optionen:  
        print("Fehlerhafte Eingabe!")
    else:
        if nutzerEingabe == schereString:
            if computerEingabe == schereString:
                print("U")
            elif computerEingabe == steinString:
                print("V")
            elif computerEingabe == papierString:
                print("G")
                gewonnen = True
        elif nutzerEingabe == steinString:
            if computerEingabe == schereString:
                print("G")
                gewonnen = True
            elif computerEingabe == steinString:
                print("U")
            elif computerEingabe == papierString:
                print("V")
        elif nutzerEingabe == papierString:
            if computerEingabe == schereString:
                print("V")
            elif computerEingabe == steinString:
                print("G")
                gewonnen = True
            elif computerEingabe == papierString:
                print("U")
        print(nutzerEingabe,"gegen",computerEingabe)