def pascal(z,s):
    if s==1 or s == z:
        return 1
    else:
        return pascal(z-1,s-1)+pascal(z-1,s)
    
z = int(input("Zeilen: "))

for i in range(1, z + 1):
    row = [str(pascal(i, j)) for j in range(1, i + 1)]
    print(" ".join(row))
