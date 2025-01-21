zahl_a = int(input("A: "))
zahl_b = int(input("B: "))

def addition_rek(zahl_a,zahl_b):
    #print(f"{zahl_a} + {zahl_b}")
    if zahl_b <= 0:
        return zahl_a
    else:
        return addition_rek(zahl_a+1,zahl_b-1)
    
def addition_alternativ(a,b):
    if b <= 0:
        return a
    return 1 + addition_alternativ(a,b-1)

print(f"{zahl_a}+{zahl_b} = {(addition_rek(zahl_a,zahl_b))}")
print(f"{zahl_a}+{zahl_b} = {(addition_alternativ(zahl_a,zahl_b))}")
