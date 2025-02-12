def null_bin(zahl=0):
    def f(x):
        return x**3-2*x**2+3*x-5
    
    untereGrenze = 0
    obereGrenze = 2

    epsilon = 0.001
    schätzung = untereGrenze +(obereGrenze-untereGrenze)/2

    while abs(f(schätzung)-zahl) >= epsilon:
        if f(schätzung)<zahl:
            untereGrenze = schätzung
        else:
            obereGrenze = schätzung
        schätzung = untereGrenze +(obereGrenze-untereGrenze)/2
    return schätzung

print(null_bin())

def null_nr(zahl=0):
    def f(x):
        return x**3-2*x**2+3*x-5
    def f2(x):
        return 3*x**2-4*x+3
    
    schätzung = 0
    epsilon = 0.001

    while abs(f(schätzung)-zahl)>=epsilon:
        schätzung = schätzung-f(schätzung)/f2(schätzung)
    return schätzung

print(null_nr())