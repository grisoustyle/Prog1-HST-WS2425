def palindrom(wort):
    print(wort)
    if len(wort) <=1:
        return True
    
    elif wort[0] != wort[-1]:
        return False
    
    return palindrom(wort[1:-1])

#print(palindrom("lagerregal"))

def satzpalindrom(satz):
    wortkette=""
    satz=satz.lower()
    for zeichen in satz:
        if zeichen not in "!,.? ":
            wortkette += zeichen
    return palindrom(wortkette)

print(satzpalindrom("Vitaler Nebel mit Sinn ist im Leben relativ."))