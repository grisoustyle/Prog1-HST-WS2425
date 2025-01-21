testset = {
    "Monitor",
    "Tastatur",
    "Maus",
    "Drucker",
    "Scanner"
}

def setlänge(set):
    print(testset)
    print(f"Anzahl Elemente: {len(set)}")
    return
setlänge(testset)

for item in testset:
    if item == "Drucker":
        print(item)

print(f"Ist Headset enthalten: {'Headset' in testset}")

testset.add("Monitor")
setlänge(testset)
#Weil Sets keine doppelten Elemente haben

testset.update(["Handy","Lampe","Gamingstuhl"])
setlänge(testset)

testset.remove("Handy")
setlänge(testset)