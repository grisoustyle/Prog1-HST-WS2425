zahl_a = int(input("A: "))
zahl_b = int(input("B: "))

def ggt_rek(a,b):
    #70 / 42 = 1 Rest 28
    rest= (a%b)
    print (f"{a}/{b} = {a//b} Rest: {rest}")
    if rest == 0:
        print(f"Gesuchtes Ergebnis: {b}")
        return b
    else:
        return ggt_rek(b,rest)

print("\nRekursiv:")
ggt_rek(zahl_a,zahl_b)

def ggt_it(a,b):

    while b != 0:
        print(f"{a}/{b} = {a//b} Rest: {a % b}")
        a, b = b, a % b #a wird b, b wird rest
        
    print(f"Gesuchtes Ergebnis: {a}")

print("\nIterativ:")
ggt_it(zahl_a,zahl_b)