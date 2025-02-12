def konsonant(wort):
    konsonanten = 0
    for buchstabe in wort:
        if wort not in "aeiou":
            konsonanten +=1
    return print(f"K:{konsonanten}")

def ualph(wort):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    neue = ""
    for zeichen in alphabet[:-1]:
        for buchstabe in wort:
            if zeichen == buchstabe and zeichen not in neue:
                neue +=zeichen
    return print(neue)

wort = str(input("Wort: "))
konsonant(wort)
ualph(wort)
