englisch = {
    "Brot":"Bread",
    "Wein":"wine",
    "Mit":"with",
    "Ich":"I",
    "essen":"eat",
    "trinken":"drink",
    "freunde":"friends",
    "und":"and",
    "von":"of",
    "rot":"red"
}

französisch = {
    "Brot": "pain",
    "Wein": "vin",
    "Mit": "avec",
    "Ich": "je",
    "essen": "mange",
    "trinken": "bois",
    "freunde": "amis",
    "Und": "et",
    "Von": "du",
    "rot": "rouge"
}
satz = "Ich essen rot Brot"
#Englisch: I drink good red wine

print(satz)
sprachwahl=int(input("1: Nach Englisch\n2: Nach Französisch "))
if sprachwahl == 1:
    sprache = englisch
elif sprachwahl ==2:
    sprache = französisch


liste_satz = satz.split()
übersetzung = ""

for wort in liste_satz:
    übersetzung += sprache[wort]+" "

print (übersetzung)