fruechte = {
    "Apfel":7,
    "Banane":9,
    "Orange":11
}

fruechte["Erdbeere"] = 10
print(fruechte)

del fruechte["Banane"]
print(fruechte)

weitere_fruechte = {
    "Kiwi":77,
    "Orange":33,
    "Mango":12
}

fruchtkiste = {

}

fruchtkiste.update(fruechte)
fruchtkiste.update(weitere_fruechte)
print(fruchtkiste)