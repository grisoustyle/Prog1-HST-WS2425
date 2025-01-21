eingabe = ""
zahler = 1
wort=""

while eingabe != "stop":
    eingabe = str(input(f"Geben Sie den {zahler} Buchstaben ein: "))
    if len(eingabe) <1 or len(eingabe)>1:
        print("Fehlerhafte Eingabe. Bitte nur 1 Buchstaben.")
    else:
        zahler+=1
        if eingabe != "stop":
            wort = wort+eingabe
                
print (f"Das Wort ist: {wort}")