deutsche_buchstabiertafel = ("Anton", "Berta", "Cäsar", "Dora", "Emil",
"Friedrich", "Gustav", "Heinrich", "Ida", "Julius", "Kaufmann", "Ludwig", "Martha",
"Nordpol", "Otto", "Paula", "Quelle", "Richard", "Siegfried", "Theodor", "Ulrich",
"Viktor", "Wilhelm", "Xanthippe", "Ypsilon", "Zacharias")

def suche_bin(wort):
    untereGrenze = 0
    obereGrenze = len(deutsche_buchstabiertafel)-1

    näherung = untereGrenze+(obereGrenze-untereGrenze)//2
    iterationen = 1
    while wort != deutsche_buchstabiertafel[näherung]:
        #print(untereGrenze,obereGrenze,näherung)
        if deutsche_buchstabiertafel[näherung] < wort:
            untereGrenze = näherung
        else:
            obereGrenze = näherung
        näherung = untereGrenze+(obereGrenze-untereGrenze)//2
        iterationen +=1

        
    return (näherung,f"Iterationen: {iterationen}")


print(suche_bin("Dora"))
#print(suche_bin("Test"))
print(suche_bin("Zacharias"))

print("-------")

def suche_lin(wort):
    index = 0
    iterationen = 1
    while wort != deutsche_buchstabiertafel[index]:
        index +=1
        iterationen+=1
        if index > len(deutsche_buchstabiertafel)-1:
            return (-1,f"Iterationen: {iterationen}")
    return (index,f"Iterationen: {iterationen}")

print(suche_lin("Dora"))
print(suche_lin("Test"))
print(suche_lin("Zacharias"))