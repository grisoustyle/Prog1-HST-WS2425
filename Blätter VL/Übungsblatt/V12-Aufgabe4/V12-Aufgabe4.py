def palindrom(wort):
    if len(wort) <=1:
        return True
    if wort[0]==wort[-1]:
        return palindrom(wort[1:-1])
    else:
        return False
    
wort = str(input("Wort: "))

print(palindrom(wort.lower()))