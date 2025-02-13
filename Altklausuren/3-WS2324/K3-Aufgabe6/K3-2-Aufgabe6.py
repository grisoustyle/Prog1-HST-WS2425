deutsche_buchstabiertafel = ("Anton", "Berta", "Cäsar", "Dora", "Emil",
"Friedrich", "Gustav", "Heinrich", "Ida", "Julius", "Kaufmann", "Ludwig", "Martha",
"Nordpol", "Otto", "Paula", "Quelle", "Richard", "Siegfried", "Theodor", "Ulrich",
"Viktor", "Wilhelm", "Xanthippe", "Ypsilon", "Zacharias")

def suche_lin(suchwort):
    index = 0
    while deutsche_buchstabiertafel[index]!=suchwort:
        index +=1
        if index>len(deutsche_buchstabiertafel)-1:
            return print(-1)
    return print(index)

suche_lin("Dora")
suche_lin("Test")
suche_lin("Zacharias")

def suche_bin(suchwort):
    untereGrenze = 0
    obereGrenze = len(deutsche_buchstabiertafel)-1
    epsilon = 1
    schätzung = untereGrenze + (obereGrenze-untereGrenze)//2

    while deutsche_buchstabiertafel[schätzung]!=suchwort:
        if deutsche_buchstabiertafel[schätzung]< suchwort:
            untereGrenze = schätzung
        else:
            obereGrenze = schätzung
        schätzung = untereGrenze + (obereGrenze-untereGrenze)//2
    return print(schätzung)

print("--")
suche_bin("Dora")
#suche_bin("Test")
#suche_bin("Zacharias")