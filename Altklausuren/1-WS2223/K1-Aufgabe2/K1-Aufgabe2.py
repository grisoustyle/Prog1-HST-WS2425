def fakultät(n):
    ergebnis = 1
    if n <=0:
        return 0
    while n>0:
        ergebnis *= n
        n-=1
    return ergebnis

print(fakultät(3))
