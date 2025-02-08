import math

def oberfläche_lin(o):
    schätzung = 0
    epsilon = 0.001
    iteration = 1
    while abs(o-4*math.pi*schätzung**2)>=epsilon:
        schätzung+=epsilon
        iteration+=1
    return schätzung,iteration

print(oberfläche_lin(1))

def oberfläche_bin(o):
    untereGrenze = 0
    obereGrenze = o
    epsilon = 0.001
    iteration=1

    schätzung = untereGrenze + (obereGrenze-untereGrenze)/2
    while abs(o-4*math.pi*schätzung**2)>=epsilon:
        if (4*math.pi*schätzung**2) < o:
            untereGrenze = schätzung
        else:
            obereGrenze = schätzung
        schätzung = untereGrenze + (obereGrenze-untereGrenze)/2
        iteration+=1
    return schätzung,iteration

print(oberfläche_bin(1))