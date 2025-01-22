"""
Übung 2
Fingerübungen
Schreiben Sie folgende kleinere Programme. 

4)	Schreiben Sie ein Programm, welches den längsten Substring in s findet, bei dem die Buchstaben in alphabetischer Reihenfolge vorkommen.
"""

eingabe = input("Geben Sie einen beliebigen String ein: ")
eingabe = eingabe.lower()


pos = 0
laengeLaengsterAlphabetischerSubstring = 0
laengsterAlphabetischerSubstring = ""

while pos < len(eingabe):
    # extrahiere Substring bis Ende ab pos
    substring = eingabe[pos:]
    alphabetischerAnfangInSubstring = substring[0]

    # starte mit dem nächsten Element
    positionInSubstring = 1
    
    while positionInSubstring < len(substring) and substring[positionInSubstring] >= substring[positionInSubstring - 1]:
        alphabetischerAnfangInSubstring += substring[positionInSubstring]
        positionInSubstring += 1

    # vergleiche mit global (bisher) längstem alphabetischem Substring
    if len(alphabetischerAnfangInSubstring) > laengeLaengsterAlphabetischerSubstring:
        laengeLaengsterAlphabetischerSubstring = len(alphabetischerAnfangInSubstring)
        laengsterAlphabetischerSubstring = alphabetischerAnfangInSubstring

    pos += 1

print("Längster Substring in alphabetischer Reihenfolge: " + laengsterAlphabetischerSubstring)
