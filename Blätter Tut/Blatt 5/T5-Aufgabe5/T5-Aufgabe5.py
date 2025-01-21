Terminplan = {
    "Montag":{
        "Vormittag":"Schlafen",
        "Nachmittag":"Essen"
    },
    "Dienstag":{
        "Vormittag":"Lernen",
        "Nachmittag":"Filme gucken"
    },
    "Mittwoch":{
        "Vormittag":"Nichts",
        "Nachmittag":"Üben"
    },
    "Donnerstag":{
        "Vormittag":"Wirtschaftsinformatik",
        "Nachmittag":"Mathematik"
    },
    "Freitag":{
        "Vormittag":"Programmierung",
        "Nachmittag":"Grundlagen BWL"
    }
}

for tag,termine in Terminplan.items():
    print(f"{tag}: {termine['Vormittag']}")

#M
