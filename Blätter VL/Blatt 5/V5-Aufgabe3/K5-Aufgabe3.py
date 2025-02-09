def div_bin(a,b):
    
    untereGrenze = 0
    obereGrenze = a
    epsilon = 0.001

    schätzung = untereGrenze + (obereGrenze-untereGrenze)/2

    while abs(schätzung*b-a)>= epsilon:
        if schätzung*b < a:
            untereGrenze = schätzung
        else:
            obereGrenze = schätzung
        schätzung = untereGrenze + (obereGrenze-untereGrenze)/2
    return schätzung
    
print(div_bin(6,2))