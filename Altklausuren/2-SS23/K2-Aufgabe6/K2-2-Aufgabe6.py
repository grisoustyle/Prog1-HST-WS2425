import math

def radius_lin(o):
    schätzung = 0
    step = 0.001
    epsilon = 0.001
    
    while abs(4*math.pi*schätzung**2-o) >= epsilon:
        schätzung+=step
    return schätzung

#print(radius_lin(5))
#frag nicht was für saft bruder

def radius_bin(o):
    untereGrenze = 0
    obereGrenze = o/2
    epsilon = 0.001

    schätzung = untereGrenze + (obereGrenze-untereGrenze)/2

    while abs(4*math.pi*schätzung**2-o)>=epsilon:
        if 4*math.pi*schätzung**2<o:
            untereGrenze = schätzung
        else:
            obereGrenze = schätzung
        schätzung = untereGrenze + (obereGrenze-untereGrenze)/2
    return schätzung

print(radius_bin(50))