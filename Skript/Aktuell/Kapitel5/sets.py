#ungeordnet -> kann nicht auf genaue positionen zugreifen, keine dopptelten Elemente

einkaufswagen = {
    "Apfel",
    "Birne",
    "Birne",
    "Tomate"
}

print(einkaufswagen)

for items in einkaufswagen:
    print(items)

einkaufswagen.add("Birne")
print(einkaufswagen)

einkaufswagen.add("Mango")
print(einkaufswagen)