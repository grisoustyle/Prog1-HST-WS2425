def fak(n):
    ergebnis = 1
    if n <= 0:
        return 1
    while n >0:
        ergebnis *= n
        n-=1
    return ergebnis

print(fak(5))