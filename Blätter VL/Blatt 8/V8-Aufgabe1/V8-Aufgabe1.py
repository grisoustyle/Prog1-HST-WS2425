text_list = [
    "Was",
    "sagt",
    "ein",
    "Informatiker",
    "wenn",
    "er",
    "auf",
    "die",
    "Welt",
    "kommt",
    "?",
    "Hallo",
    "Welt",
    "!"
]

print(f"\nOriginal:\n{text_list}")

kleine_liste =[]

for wort in text_list:
    kleine_liste.append(wort.lower()) #sonst wäre bsp. "wenn < Hallo"
#print(kleine_liste)

for aktuelles_wort in range(len(kleine_liste)): #grabt wort 1
    for vergleichs_wort in range(aktuelles_wort + 1, len(kleine_liste)): #grabt wort 1+1 = wort 2
        wort_1 = kleine_liste[aktuelles_wort]
        wort_2 = kleine_liste[vergleichs_wort]

        if len(wort_1) > len(wort_2): #1 länger als 2
            kleine_liste[aktuelles_wort], kleine_liste[vergleichs_wort] = wort_2, wort_1 #dann tauschen

        #wenn wort1 < wort2: passt sowieso

        elif len(wort_1) == len(wort_2) and wort_1 > wort_2: #wenn gleich lang UND 1 alphabetisch größer
            kleine_liste[aktuelles_wort], kleine_liste[vergleichs_wort] = wort_2, wort_1 #dann tauschen

print(f"\nNeu:\n{kleine_liste}")
