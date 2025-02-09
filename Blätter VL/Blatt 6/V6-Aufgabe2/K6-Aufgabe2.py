#f(x)= x^3 - 2x^2 + 3x - 5

def nullstelle_nr(zahl=0):
    def f(x):
        return x**3 - 2*x**2 + 3*x - 5
    def f2(x):
        return 3*x**2 - 4*x + 3
    
    epsilon = 0.001
    schätzung = 1
    iteration = 1

    while abs(f(schätzung)-zahl)>=epsilon:
        schätzung = schätzung-f(schätzung)/f2(schätzung)
        iteration +=1
    return schätzung,iteration

print(nullstelle_nr())

def nullstelle_bin(zahl=0):
    def f(x):
        return x**3 - 2*x**2 + 3*x - 5
    
    untereGrenze = 0
    obereGrenze = 2
    epsilon = 0.001
    iteration = 1

    schätzung = untereGrenze + (obereGrenze-untereGrenze)/2

    while abs(f(schätzung)-zahl)>=epsilon:
        if f(schätzung) < zahl:
            untereGrenze = schätzung
        else:
            obereGrenze = schätzung
        schätzung = untereGrenze + (obereGrenze-untereGrenze)/2
        iteration +=1
    return schätzung,iteration

print(nullstelle_bin())