Terminplan = {
    "Montag":"Schlafen",
    "Dienstag":"Essen",
    "Mittwoch":"Langweilen",
    "Donnerstag":"Wirtschaftsinformatik",
    "Freitag":"Programmierung"
}

print(Terminplan["Montag"])

Terminplan["Donnerstag"] = ["Statistik","Grundlagen BWL","Finanzierung"]
print(Terminplan)

print(Terminplan["Donnerstag"][2])