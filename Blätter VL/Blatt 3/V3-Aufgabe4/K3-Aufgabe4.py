def summe(n):
    ergebnis = 0
    for zahl in range(1,n+1):
        ergebnis += zahl
    return ergebnis

print(summe(9))

def n_summe(n):
    ergebnis = 0
    for i in range(n,101,n):
        ergebnis += i
    return ergebnis

print(n_summe(2))

def prim(n):
    return

def teilbar(n):
    for zahl in range (1,101):
        if zahl%n == 0:
            print(zahl)

teilbar(2)