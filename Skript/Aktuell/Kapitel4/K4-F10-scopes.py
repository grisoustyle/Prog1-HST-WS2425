def geradeZahl(i, ausgabeText="Hallo"): #Standardbelegung von ausgabeText = "Hallo"
    """
    Input: i, Zahl
    Returns True if i is even, otherwise False
    """
    print(ausgabeText)
    print("Wir sind in der Funktion geradeZahl und testen die Zahl " + str(i))
    return i % 2 == 0

i = int(input("Testzahl: "))

print(geradeZahl(i, "Halli")) #Wenn "Halli" (als ausgabeText) mitgegeben wird, wird die Standardbelegung "Hallo" überschrieben
print(geradeZahl(i)) #Kein ausgabeText mitgegeben -> Standardbelegung "Hallo" wird genommen

