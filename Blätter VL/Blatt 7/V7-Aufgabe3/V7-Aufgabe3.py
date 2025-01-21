eingabe = str(input("Wort: ")).lower()

def palindrom_check(wort):
    
    if len(wort)>1:
        print(f"\nAufruf von Funktion mit: {wort}")
        print(f"Vergleich: {wort[0]} mit {wort[-1]}")

    if len(wort)<=1:
        return True
    
    if wort[0] != wort[-1]:
        print("Durchlauf mit Erster und letzter Buchstabe unterschiedlich!")
        return False
    
    
    return palindrom_check(wort[1:-1])
            


def satzpalindrom(wort):
    wort_ohne_leer=""
    for zeichen in wort:
        if zeichen not in (" " , "?" , "." , "," , "!", "(", ")", ":"):
            wort_ohne_leer += zeichen
    #print (wort_ohne_leer)
    return palindrom_check(wort_ohne_leer)


auswahl = int(input("1: Palindrom\n2: Satzpalindrom\n"))
if auswahl == 1:
    print(f"\nErgebnis: ({eingabe}) = {(palindrom_check(eingabe))}")
if auswahl == 2:
    print(f"\nErgebnis: ({eingabe}) = {(satzpalindrom(eingabe))}")

#Bei der Edna redete der andere Dieb.
#Vitaler Nebel mit Sinn ist im Leben relativ.

#lagerregal
#reliefpfeiler