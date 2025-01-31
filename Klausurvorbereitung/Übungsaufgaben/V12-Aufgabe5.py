def konsonanten(wort):
    konsonanten_zahl = 0
    for buchstabe in wort:
        if buchstabe not in ["a","e","i","o","u"]:
            konsonanten_zahl+=1
    return konsonanten_zahl

'''def u_alphabet(wort):
    wortliste = sorted(wort)
    return wortliste[::-1]'''

def u_alphabet_2(wort):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ausgabe=""
    for buchstabe in alphabet:
        if buchstabe in wort:
            ausgabe=buchstabe + ausgabe
    return ausgabe



wort = str(input("Wort: ").lower())

print(konsonanten(wort))
print(u_alphabet_2(wort))