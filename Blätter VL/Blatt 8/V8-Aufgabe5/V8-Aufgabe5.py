"""Übung 1
Chatten like Kant
Um unsere Freunde zu beeindrucken, möchten wir uns gerne insbesondere beim Chatten
so eloquent wie die großen Philosophen ausdrücken. Praktischerweise gibt es auf 
mobilen Geräten häufig einen Vorschlag-Mechanismus, der während der Texteingabe
automatisch wahrscheinliche Kandidaten für die nächsten Worte auflistet. 
Anstatt der üblichen Vorschläge von iOS oder Android würden wir hier aber nun 
gerne Wortvorschläge auf Basis des statistischen Auftretens von Wortfolgen aus 
philosophischen Werken erhalten. Ziel dieser Übung ist es daher ein kleines Programm 
zu schreiben, welches die Wortfolgen in einem philosophischen Werk analysiert und auf 
dieser Basis Wortkandidaten vorschlägt.
"""
from pathlib import Path

def lies_datei_als_gefilterte_wort_liste():
    """Liest Textdatei ein und gibt Liste an Wörtern gefiltert zurück
    """
    p = Path(__file__).with_name('kant.txt')
    fobj = open(p, encoding="utf-8")

    input_text = ""
    for line in fobj:
        lower_text = line.rstrip().lower()
        for char in lower_text:
            if char in " abcdefghijklmnopqrstuvwxyzäöüß-":
                input_text += char
        input_text += " "
    fobj.close()

    return input_text.split()

def sortiere_dictionary_absteigend_nach_wert(input_dict):
    """Sortiert Dictionary nach dem Wert (value)

    Args:
        input_dict (dict): Dictionary (key/value)

    Returns:
        dict: Sortiertes Dictionary nach value
    """
    return dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=True))

# Start Programm
liste_woerter = lies_datei_als_gefilterte_wort_liste()

#Anzahl jeweiliger Wörter zählen:
wort_zähler_dictionary= {}
for wort in liste_woerter:
    if wort in wort_zähler_dictionary:
        wort_zähler_dictionary[wort]+=1
    else:
        wort_zähler_dictionary[wort]=1



# Testweise Ausgabe der Liste an Wörtern
print(liste_woerter)

# Beispiel-Code für die Sortierung eines Dictionary nach seinen Werten (values, nicht keys!)
test_dict = {"wissenschaft":1, "dogmatisch":8, "urteilen":5}
print(test_dict)
test_dict = sortiere_dictionary_absteigend_nach_wert(test_dict)
print(test_dict)

print(wort_zähler_dictionary)

for wort in wort_zähler_dictionary:
    if wort_zähler_dictionary[wort] >= 100:
        print(f"{wort}: {wort_zähler_dictionary[wort]}")