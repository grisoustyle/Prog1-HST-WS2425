def kubik_nr(zahl):
    def f(x):
        return x**3
    def f_abl(x):
        return 3*x**2
    
    epsilon = 0.001

    schätzung = zahl/3

    while abs(f(schätzung)-zahl)>=epsilon:
        schätzung = schätzung -(f(schätzung)-zahl)/f_abl(schätzung)
    
    return schätzung

print(kubik_nr(9))

def kubik_bin(zahl):
    def f(x):
        return x**3
    
    epsilon = 0.001
    untereGrenze = 0
    obereGrenze = zahl/3
    näherung = untereGrenze + (obereGrenze-untereGrenze)/2

    while abs(f(näherung)-zahl)>=epsilon:
        if f(näherung) < zahl:
            untereGrenze = näherung
        else:
            obereGrenze = näherung
        näherung = untereGrenze + (obereGrenze-untereGrenze)/2
    return näherung

print(kubik_bin(9))