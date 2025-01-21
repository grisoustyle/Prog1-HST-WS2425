zahl = int(input("Zahl eingeben: "))

#02-Folie 42 Kubikwurzeln Guess and Check (auch negativ)
def kubikwurzel_gc(zahl):
    schatzwert = 0

    while (schatzwert**3) < abs(zahl):
        schatzwert +=1
    if schatzwert**3 != abs(zahl):
        print(f"{zahl} hat keine ganzzahlige Kubikwurzel!")
    else:
        if zahl < 0:
            schatzwert = -schatzwert
        print(f"Kubikwurzel von {zahl} ist {schatzwert}")

#02-Folie 46 Kubikwurzeln Guess and Check eleganter (nur positiv)
def kubikwurzel_gcv2(zahl):
    for schatzung in range(zahl+1):
        if schatzung**3==zahl:
            print(f"Kubikwurzel von {zahl} ist {schatzung}")

#02-Folie 47 Kubikwurzeln Guess and Check eleganter (auch negativ)
def kubikwurzel_gcv3(zahl):
    schatzung = 0
    for schatzung in range(abs(zahl)+1):
        if schatzung**3 >= abs(zahl):
            break
    if schatzung**3 != abs(zahl):
        print(f"{zahl} hat keine ganzzahlige Kubikwurzel!")
    else:
        if zahl < 0:
            schatzung = -schatzung
        print(f"Kubikwurzel von {zahl} ist {schatzung}")