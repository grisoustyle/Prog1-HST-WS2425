def potenzieren (zahl,potenz): #2^3 = 2*2^2 = 2*2*2^1 = 2*2*2*2^0 = 2*2*2*1 
    #print(zahl,potenz)
    if potenz >0:
        return zahl*(potenzieren(zahl,(potenz-1)))
    if potenz == 0:
        return 1
    

zahl = int(input("Basis: "))
potenz = int(input("Exponent: "))

print(f"{zahl}^{potenz} = {(potenzieren(zahl,potenz))}")