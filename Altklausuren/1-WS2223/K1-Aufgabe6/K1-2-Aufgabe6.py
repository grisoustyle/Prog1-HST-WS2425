import math

def radius_lin(a):
    schätzung = 0
    step = 0.001
    while schätzung**2*math.pi < a:
        schätzung+=step
    return schätzung

print(radius_lin(5))

def radius_bin(a):
    untereGrenze = 0
    obereGrenze = a/2
    epsilon = 0.001

    schätzung = untereGrenze + (obereGrenze-untereGrenze)/2

    while abs(schätzung**2*math.pi-a)>=epsilon:
        if schätzung**2*math.pi<a:
            untereGrenze = schätzung
        else:
            obereGrenze = schätzung
        schätzung = untereGrenze +(obereGrenze-untereGrenze)/2
    return schätzung

print(radius_bin(5))