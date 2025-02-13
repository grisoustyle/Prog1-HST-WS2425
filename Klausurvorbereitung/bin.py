'''Aufgabe 6 – Binäre Suche (12 Punkte)

Implementieren Sie eine Funktion binaere_suche(liste, wert), 
die eine sortierte Liste und einen gesuchten Wert entgegennimmt und
die Position des Wertes in der Liste zurückgibt. Falls der Wert nicht vorhanden ist,
soll -1 zurückgegeben werden.'''

def bin_s(liste,wert):
    untereGrenze = 0
    obereGrenze = len(liste)-1

    schätzung = untereGrenze + (obereGrenze-untereGrenze)//2
    epsilon = 1

    while abs(liste[schätzung]-wert)>=epsilon:
        if liste[schätzung]<wert:
            untereGrenze = schätzung
        else:
            obereGrenze = schätzung
        schätzung = untereGrenze + (obereGrenze-untereGrenze)//2
        return -1
    return schätzung

print(bin_s([1, 3, 5, 7, 9], 5))
print(bin_s([1, 3, 5, 7, 9], 4))