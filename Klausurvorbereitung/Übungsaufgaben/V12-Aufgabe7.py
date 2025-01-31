def div_lin(a,b):
    ergebnis = a
    step = 0.001
    
    while b*step<=a:
        step+=0.001
    return step

print(div_lin(10,2))

def div_bin(a,b):
    untereGrenze = 0
    obereGrenze = a
    epsilon = 0.001
    näherung = untereGrenze + (obereGrenze-untereGrenze)/2

    while abs((näherung*a)-b) <= epsilon:
        if näherung*a < b:
            untereGrenze = näherung
        if näherung*a > b:
            obereGrenze = näherung

        näherung = untereGrenze + (obereGrenze-untereGrenze)/2
    return näherung

print(div_bin(10,2))