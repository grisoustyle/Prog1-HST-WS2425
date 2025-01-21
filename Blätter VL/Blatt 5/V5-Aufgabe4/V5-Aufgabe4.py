gefunden = False
buchstabe= str(input("Buchstabe eingeben: "))
wort = "".join(sorted(str(input("Wort eingeben: ")))) #sorted sortiert alphabetisch als einzelne str in liste; .join fügt wieder zu einem wort zsm
#wort = "aabbbbcccfggghiklmnxz"

obergrenze= len(wort)-1
untergrenze = 0
print(f"Alphabetisch sortiertes Wort: {wort}\n")

while untergrenze <= obergrenze:
    wortmitte=(untergrenze+obergrenze)//2 #index mitte
    print(f"Prüfung von {wort[wortmitte]} mit {buchstabe} - Bereich:({untergrenze},{obergrenze}) {wort[untergrenze:obergrenze+1]}")

    if wort[wortmitte]==buchstabe: #buchstabe in wort am index wortmitte
        gefunden = True
        break

    elif buchstabe < wort[wortmitte]:
        obergrenze = wortmitte-1

    else: #buchstabe > wortmitte
        untergrenze = wortmitte+1


if gefunden:
    print(f"\nWort {wort} enthält Buchstabe {buchstabe}.\n")
else:
    print(f"\nWort {wort} enthält Buchstabe {buchstabe} nicht.\n")

