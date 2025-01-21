satz = (
    "there",
    "is",
    "no",
    "way",
    "a",
    "bee",
    "should", 
    "be",
    "able",
    "to",
    "fly"
)

print(satz[:2])

#del satz[0]; geht nich, tupel lässt nich löschen

print(satz)
liste =[]

for element in satz:
    liste.append(element)

del liste[0]
print(liste)

satz = tuple(liste)
print(satz)