"""
Übung 4
Wurzelziehen durch Guess-and-Check 
Wir haben in der letzten Vorlesung die Kubikwurzel von beliebigen ganzzahligen
Werten ermittelt, indem wir einfach alle möglichen Werte von Null startend geprüft haben. 

1) Wir möchten nun analog die Quadratwurzel einer beliebigen Zahl mithilfe der linearen Suche bestimmen. 
Bitte implementieren Sie die Lösung als Guess-and-Check-Verfahren.
"""

benutzer_eingabe = int(input("Bitte einen ganzzahligen Wert eingeben: "))

ans = 0

while ans**2 < benutzer_eingabe:
    ans = ans + 1
    
if ans**2 != benutzer_eingabe:
    print(str(benutzer_eingabe) + " hat keine ganzzahlige Quadratwurzel!")
else:
    print("Quadratwurzel von " + str(benutzer_eingabe) + " ist " + str(ans))
    print("Gegenprobe: " + str(ans) + "² = " + str(ans**2))

"""
Übung 4
Wurzelziehen durch Guess-and-Check 
Wir haben in der letzten Vorlesung die Kubikwurzel von beliebigen ganzzahligen
Werten ermittelt, indem wir einfach alle möglichen Werte von Null startend geprüft haben. 

1) Wir möchten nun analog die Quadratwurzel einer beliebigen Zahl mithilfe der linearen Suche bestimmen. 
Bitte implementieren Sie die Lösung als Guess-and-Check-Verfahren.

2) Bitte adaptieren Sie den Code für die Quadratwurzel- und Kubikwurzel-Suche derart, 
dass die Lösung nicht auf ganzzahlige Werte als Lösung beschränkt ist. 
"""

x = float(input("Bitte einen Wert eingeben: "))

ans = 5.96
stepSize = 0.01
epsilon = 0.001

while abs(ans**2 - x) > epsilon:
    ans = ans + stepSize


print("Quadratwurzel von " + str(x) + " ist annäherungsweise " + f"{ans:>.2f}")
print("Gegenprobe: " + f"{ans:>.2f}" + "² = " + f"{ans**2:>.2f}")
