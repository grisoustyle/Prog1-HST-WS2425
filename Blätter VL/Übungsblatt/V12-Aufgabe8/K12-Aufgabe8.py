import math

'''def radius_lin(volumen):
    def f(x):
        return 4/3*math.pi*x**3
    schätzung = 0
    epsilon = 0.001

    while abs(f(schätzung)-volumen) >= epsilon:
        schätzung+=epsilon
    return schätzung'''
#???????????????????????

def radius_bin(volumen):
    def f(x):
        return 4/3*math.pi*x**3
    
    untereGrenze = 0
    obereGrenze = volumen

    epsilon = 0.001

    schätzung = untereGrenze + (obereGrenze-untereGrenze)/2
    while abs(f(schätzung)-volumen) >= epsilon:
        if f(schätzung)<volumen:
            untereGrenze = schätzung
        else:
            obereGrenze = schätzung
        schätzung = untereGrenze + (obereGrenze-untereGrenze)/2
    return schätzung


print(radius_bin(100))
#print(radius_lin(100))