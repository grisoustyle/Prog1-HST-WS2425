#Newton Raphson:

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


#Binäre Suche:

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


#Lineare Suche

def kubik_lin(zahl):
    def f(x):
        return x**3
    
    schätzung = 0
    epsilon = 0.001

    while f(schätzung)<=zahl:
        schätzung+=epsilon
    return schätzung

print(kubik_lin(9))