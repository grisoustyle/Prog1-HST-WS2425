alphabet="abcdefghijklmnopqrstuvwxyz"

def codieren(wort,verschiebung):
    verschlüsselt = ""
    for buchstabe in wort:
        alt_index = alphabet.index(buchstabe)
        neu_index = (alt_index+verschiebung)%26
        verschlüsselt +=alphabet[neu_index]
    return verschlüsselt

print(codieren("testwort",1))

def decodieren(wort,verschiebung):
    entschlüsselt = ""
    for buchstabe in wort:
        alt_index = alphabet.index(buchstabe)
        neu_index = (alt_index-verschiebung)%26
        entschlüsselt +=alphabet[neu_index]
    return entschlüsselt

print(decodieren(codieren("kraftfahrzeughaftpflichtversicherung",5),5))