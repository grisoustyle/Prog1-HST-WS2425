#f(x)= x^3 - 2x^2 + 3x - 5

def nullstelle(zahl=0):
    def f(x):
        return x**3 - 2*x**2 + 3*x - 5
    def f2(x):
        return 3*x**2 - 4*x + 3
    
    epsilon = 0.001
    schätzung = 1

    while abs(f(schätzung)-zahl)>=epsilon:
        schätzung = schätzung-f(schätzung)/f2(schätzung)
    return schätzung

print(nullstelle())