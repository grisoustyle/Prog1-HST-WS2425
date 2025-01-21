'''Erstellen Sie ein Programm, welches das Vorkommen von Wörtern in einem beliebigen Text 
analysiert und die Häufigkeit pro Wort ausgibt. Satzzeichen und Groß-/Kleinschreibung soll hierbei 
ignoriert werden. (10 Punkte)'''

#Das ist ein Test. Das ist nur ein Test.

from aufgabe03 import entferne_sonderzeichen


satz = entferne_sonderzeichen(str(input("Welcher text soll analysiert werden? ")))

satzliste = satz.split( )

haeufigkeit = {

}

for wort in satzliste:
    if wort in haeufigkeit:
        haeufigkeit[wort] += 1
    else:
        haeufigkeit[wort] = 1

print("\nAntwort:")
for item in haeufigkeit:
    print(f"{item} - {haeufigkeit[item]}")
