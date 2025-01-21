zahl_a = int(input("\nZahl a angeben: "))
zahl_b = int(input("Zahl b angeben: "))
auswahl = str(input("\nWelche Rechenoperation soll ich ausführen?\nWählen Sie 'a' für Addition, 's' für Subtraktion, 'm' für Multiplikation und 'd' für Division: "))

def addition(zahl_a=0,zahl_b=0): #5 + 3 = 5+1,+1,+1 (3-1,-1,-1)
    while zahl_b > 0:
        zahl_a +=1
        zahl_b -=1
    return(zahl_a)

def multiplikation(zahl_a=0,zahl_b=0):
    ergebnis = 0
    while zahl_b > 0:
        ergebnis += zahl_a
        zahl_b -= 1
    return(ergebnis)

def subtraktion(zahl_a=0,zahl_b=0): #5 - 3 = - (-5+3) = -(-2) = 2
    ergebnis = addition(-zahl_a,zahl_b)
    return(-ergebnis)

def division(zahl_a, zahl_b): #84 / 2 = X * 2 = 84 -> Wie viele X * 2 damit 84??
    x = 0
    while multiplikation(x + 1, zahl_b) <= zahl_a:
        print(f"{x}*{zahl_b} =? {zahl_a}")
        x += 1
    return x
#prob: nur ints & keine negativen 


if auswahl == "a":
    ergebnis = (addition(zahl_a,zahl_b))
    print (f"\n{zahl_a} + {zahl_b} = {ergebnis}")
elif auswahl == "m":
    ergebnis =(multiplikation(zahl_a,zahl_b))
    print (f"\n{zahl_a} * {zahl_b} = {ergebnis}")
elif auswahl == "s":
    ergebnis= (subtraktion(zahl_a,zahl_b))
    print (f"\n{zahl_a} - {zahl_b} = {ergebnis}")
elif auswahl == "d":
    ergebnis =(division(zahl_a,zahl_b))
    print (f"\n{zahl_a} / {zahl_b} = {ergebnis}")