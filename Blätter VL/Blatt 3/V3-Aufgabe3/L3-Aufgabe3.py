"""
Übung 3
Einmaleins

Schreiben Sie ein Programm, welches die Zahlen von 1 bis 100 in einer 10x10 Matrix ausgibt. 

Hinweis: Python unterstützt die Formatierung von Strings bei der Ausgabe. 
So gibt beispielsweise folgender Befehl den Wert der Variable value vom Typ int rechtsbündig mit vier Stellen aus. 

# Formatierung des Werts value rechtsbündig mit vier Stellen
str("{:>4}").format(value)

Mehr Formatierungsmöglichkeiten finden Sie in der Python Dokumentation  
"""
#Musterlösung:
for i in range(0, 10):
    textZeile = ""
    for j in range(1, 11):
        value = i * 10 + j
        textZeile += str("{:>4}").format(value)
    print(textZeile)



#Vorlesungslösung:
textzeile = ""
for value in range(1, 101):
    textzeile += str(value)
    if (value % 10) == 0:
        textzeile += "\n"
    else:
        textzeile += " "
print(textzeile)


for mult_1 in range(0, 10):
    textzeile = ""
    for mult_2 in range(1, 11):
        textzeile += str((mult_1 * 10 + mult_2)) + " "
    print(textzeile)