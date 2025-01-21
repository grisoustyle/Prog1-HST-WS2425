Einkaufsliste= {
    "Gurke",
    "Avocado",
    "Spuelmittel",
    "Locher",
    "Salami"
}
print(Einkaufsliste)
#print(Einkaufsliste[0]); Geht nicht weil Sets keine Indexierung haben weil keine feste Reihenfolge

Einkaufsliste.add("Bier")
print(Einkaufsliste)
#random reihenfolge

Einkaufsliste.update(["Wasser","Avocado","Zucker"])
print(Einkaufsliste)

Einkaufsliste.remove("Wasser")
print(Einkaufsliste)