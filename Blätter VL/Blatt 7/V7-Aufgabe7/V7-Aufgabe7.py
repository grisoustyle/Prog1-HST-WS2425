def pascal_dreieck (z,s):
    if s == 1 or s == z:
        return 1 
    return pascal_dreieck(z-1,s-1)+(pascal_dreieck(z-1,s))

zeilen = int(input("Zeilen: "))

for i in range(1, zeilen + 1):
    row = [str(pascal_dreieck(i, j)) for j in range(1, i + 1)]
    print(" ".join(row))