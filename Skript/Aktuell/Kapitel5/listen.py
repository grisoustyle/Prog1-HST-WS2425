einkaufswagen = [
    "Apfel",
    "Banane",
    "Tomate",
    "Kuchen"
]

print(einkaufswagen[0])

einkaufswagen[0] = "Möhrensaft"
print(einkaufswagen)

einkaufswagen.append("Marmelade")
print(einkaufswagen)

for item in einkaufswagen:
    print(item)

del(einkaufswagen[2])
print(einkaufswagen)

einkaufswagen2 = [
    "Bier",
    "Aperol"
]

warteschlange_an_kasse = [einkaufswagen,einkaufswagen2]
print(warteschlange_an_kasse)

print(warteschlange_an_kasse[0][1])
print(warteschlange_an_kasse[1][1])

warteschlange_an_kasse[1].append("Whiskey")
print(warteschlange_an_kasse)