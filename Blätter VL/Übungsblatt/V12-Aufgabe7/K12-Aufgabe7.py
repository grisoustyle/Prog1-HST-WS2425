def div_lin(a,b):
    ergebnis = 1
    epsilon = 0.001

    while b*ergebnis <= a:
        ergebnis+=epsilon
    return print(ergebnis)

div_lin(10,2)

'''def div_bin(a,b):
    def f(x):
        return x*b
    
    untereGrenze = 0
    obereGrenze = a

    schätzung = untereGrenze + (obereGrenze - untereGrenze)/2
    epsilon = 0.001

    while abs(f(schätzung)-a) >= epsilon:
        if f(schätzung) < b:
            untereGrenze = schätzung
        else:
            obereGrenze = schätzung
        schätzung = untereGrenze + (obereGrenze - untereGrenze)/2
    return schätzung

print(div_bin(5,3))'''
#the fuck??