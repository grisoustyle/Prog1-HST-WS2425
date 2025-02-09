def kubikwurzel_nr(zahl):
    epsilon = 0.001
    iteration = 1
    def f(x):
        return x**3
    def f2(x):
        return 3*x**2
    
    schätzung = zahl/3

    while abs(f(schätzung)-zahl)>=epsilon:
        schätzung = schätzung- (f(schätzung)-zahl)/f2(schätzung)
        iteration +=1

    return schätzung,iteration

print(kubikwurzel_nr(27))

def kubikwurzel_bin(zahl):
    untereGrenze = 0
    obereGrenze = zahl/3

    epsilon = 0.001
    iteration = 1

    schätzung = untereGrenze + (obereGrenze-untereGrenze)/2
    while abs(schätzung**3-zahl)>=epsilon:
        if schätzung**3 < zahl:
            untereGrenze = schätzung
        else:
            obereGrenze = schätzung
        schätzung = untereGrenze+(obereGrenze-untereGrenze)/2
        iteration+=1
    return schätzung,iteration

print(kubikwurzel_bin(27))


