def zahlenvergleich(x,y):
    if x <= y:
        return x
    elif x > y:
        return y
    else:
        return "Fehler"
    
kleinerezahl = zahlenvergleich(
    x = int(input("x eingeben: ")),
    y = int(input("y eingeben: "))
    )

print(f"{kleinerezahl} ist die kleinere Zahl.")