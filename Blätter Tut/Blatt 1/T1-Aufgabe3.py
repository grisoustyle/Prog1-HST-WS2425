#A3
temp = input(str("Geben Sie die Temperatur an: "))
wetter = input(str("Geben Sie das Wetter an: "))
if temp == "warm":
    if wetter == "regnerisch":
        print("Ich empfehle ein T-Shirt und einen Schirm.")
    elif wetter == "verschneit":
        print("Diese Wetter Kombination existiert nicht.")
    elif wetter == "sonnig":
        print("Ich empfehle ein T-Shirt und eine kurze Hose.")
    else:
        print("Fehlerhafte Wetterangabe.")
elif temp == "kalt":
    if wetter == "regnerisch":
        print("Ich empfehle eine dicke Jacke und einen Schirm.")
    elif wetter == "verschneit":
        print("Ich empfehle eine dicke Jacke und festes Schuhwerk.")
    elif wetter == "sonnig":
        print("Ich empfehle eine dicke Jacke.")
    else:
        print("Fehlerhafte Wetterangabe.")
else:
    print("Fehlerhafte Temperaturangabe")