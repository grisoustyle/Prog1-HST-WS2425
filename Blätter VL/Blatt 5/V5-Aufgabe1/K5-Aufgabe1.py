
def raten():
    untereGrenze = 0
    obereGrenze = 100
    erraten = False

    while not erraten:
        schätzung = untereGrenze + (obereGrenze-untereGrenze)//2
        antwort = str(input(f"Ist die Zahl {schätzung}? "))
            
        if antwort == "k":
            erraten = True
    
        elif antwort == 'h':
            untereGrenze = schätzung

        elif antwort == 'n':
            obereGrenze = schätzung

    return print(f"Die Zahl war {schätzung}")

raten()