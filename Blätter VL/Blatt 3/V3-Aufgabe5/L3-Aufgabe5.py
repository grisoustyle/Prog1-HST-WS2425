"""
Übung 5
Das Heron-Verfahren
In der ersten Vorlesung haben wir das Heron-Verfahren kennengelernt. 
Implementieren Sie bitte das Heron-Verfahren zur Bestimmung der Wurzel 
aus einer Zahl x bei gegebenem Startwert g. Sowohl x als auch g sind 
Eingabe des Nutzers. Terminieren Sie den Algorithmus, wenn die 
Differenz d zwischen der letzten und der aktuellen Nähe-rung d < 10-5 ist, 
spätestens aber nach 5 Iterationen. Geben Sie in jeder Iteration Ihre 
Zwischenergebnisse aus. 

Versuchen Sie eigenständig in der Python-Dokumentation (Link siehe Übung 3) 
herauszufinden, wie man die Werte für g in jeder Iteration gut lesbar formatiert ausgibt. 
"""

x = int(input("Bestimme die Wurzel aus: "))
g = int(input("Starte mit folgendem Wert: "))

iteration = 1

while abs(g * g - x) > 10**-5 and iteration < 6:
    g = (x / g + g) / 2
    print("Iteration " + str(iteration) + " - Wert von g: " + f"{g:>6.4f}")
    iteration += 1

print("Die Wurzel aus " + str(x) + " beträgt näherungsweise " + f"{g:>6.4f}")
