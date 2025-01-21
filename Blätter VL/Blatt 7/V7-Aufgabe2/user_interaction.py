import kreis_kugel

radius = int(input("\nRadius angeben: "))
auswahl = str(input("\nZu berechnenden Wert auswählen:\n'f': Fläche\n'u': Umfang\n'o': Oberfäche\n'v': Volumen\n---\nAuswahl: "))
if auswahl == "f":
    print (kreis_kugel.flaeche(radius))
elif auswahl == "u":
    print (kreis_kugel.umfang(radius))
elif auswahl == "o":
    print (kreis_kugel.oberflaeche(radius))
elif auswahl == "v":
    print (kreis_kugel.volumen(radius))
else:
    print("Ungültige Eingabe.")