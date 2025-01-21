###
# ALTERNATIVLÖSUNG!!
# BENUTZT KEINE BINÄRE SUCHE!
###

import random

print("\nDenke dir eine Zahl zwischen 0 und 100 aus und merke sie Dir.")
erraten = False
untergrenze = 0
obergrenze = 100


while not erraten:
    zahl = random.randint(untergrenze,obergrenze)
    print(f"Ist die geheime Zahl {zahl}?")
    antwort = str(input("k für korrekt, h für höher, n für niedriger - "))
    if antwort == "k":
        erraten = True
    elif antwort == "h":
        untergrenze = zahl
        print (f"\nNeuer Suchbereich: ({untergrenze},{obergrenze})")
    elif antwort == "n":
        obergrenze = zahl
        print (f"\nNeuer Suchbereich: ({untergrenze},{obergrenze})")
    else:
        print (f"\nFehlerhafte Antwort. Mögliche Optionen: \
               \nk für korrekt, \nh für höher, \nn für niedriger. \
               \nDie Zahl wird weiterhin im Bereich ({untergrenze},{obergrenze}) gesucht.")


print (f"Die Zahl {zahl} wurde erraten in einem Suchbereich von {untergrenze} bis {obergrenze}.")