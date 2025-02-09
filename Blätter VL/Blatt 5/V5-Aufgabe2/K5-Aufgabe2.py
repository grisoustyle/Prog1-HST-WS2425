def quadratw(zahl):
    untereGrenze = 0
    obereGrenze = zahl/2
    epsilon = 0.001

    schätzung = untereGrenze + (obereGrenze-untereGrenze)/2

    while abs(schätzung**2-zahl)>=epsilon:
        if schätzung**2 < zahl:
            untereGrenze = schätzung
        else:
            obereGrenze = schätzung
        schätzung = untereGrenze + (obereGrenze-untereGrenze)/2
    return schätzung

print(quadratw(9))

def kubikw(zahl):

    def f(x):
        return x**3
    
    if zahl > 1:
        untereGrenze = 0
        obereGrenze = zahl/2
    else:
        untereGrenze = zahl/2
        obereGrenze = 0
    epsilon = 0.001
    
    schätzung = untereGrenze + (obereGrenze-untereGrenze)/2
    while abs(f(schätzung)-zahl)>=epsilon:
        if f(schätzung) < zahl:
            untereGrenze = schätzung
        else:
            obereGrenze = schätzung
        schätzung = untereGrenze + (obereGrenze-untereGrenze)/2
    return (-1*schätzung)

print(kubikw(-9))
