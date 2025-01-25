# Einbinden der Bibliothek 
import random 
 
vokabeln = { 
    "hallo": "hello", 
    "bitte": "please", 
    "ja": "yes", 
    "nein": "no", 
    "hund": "dog", 
    "katze": "cat", 
    "essen": "eat", 
    "trinken": "drink", 
    "schlafen": "sleep", 
} 
 
# Wählt ein zufälliges Wort aus der Vokabelliste aus 
#key = random.choice(list(vokabeln.keys())) 
 
# Ausgabe des Wortpaares 
#print("Deutsch: ", key) 
#print("Englisch: ", vokabeln[key])


def test():
    progressbar = "[_____]"
    counter = 1
    while counter < 6:
        key = random.choice(list(vokabeln.keys())) 
        antwort = str(input(f"{progressbar} {key} : "))
        
        if antwort == vokabeln[key]:
            progressbar = "[" + counter*"X" + (5-counter)*"_" + "]"
            counter +=1
        else:
            print(f"Falsch, richtige Antwort wäre gewesen: {vokabeln[key]}")
    print(f"{progressbar} Gratulation! Gut gemacht!")

test()