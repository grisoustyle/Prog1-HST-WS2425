untergrenze = 0
obergrenze = 100
erraten = False

while not erraten:
    zahl = (obergrenze+untergrenze)//2

    antwort = str(input(f"\nIst die Zahl {zahl}?\nk: korrekt; h: höher; n: niedriger. - ")) #50?

    if antwort == "k": #ja. 50
        print(f"Die Zahl war {zahl}.")
        erraten = True

    elif antwort == "n": #niedriger, -> [0;49]
        obergrenze = (zahl-1)
    
    elif antwort == "h": #höher, -> [51;100]
        untergrenze = (zahl+1)
    
    else:
        print("Fehlerhafte Eingabe.")
        