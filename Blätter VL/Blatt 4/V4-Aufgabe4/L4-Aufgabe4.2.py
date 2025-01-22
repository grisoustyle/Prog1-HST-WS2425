"""
Übung 4
Wurzelziehen durch Guess-and-Check 
Wir haben in der letzten Vorlesung die Kubikwurzel von beliebigen ganzzahligen
Werten ermittelt, indem wir einfach alle möglichen Werte von Null startend geprüft haben. 

1) Wir möchten nun analog die Quadratwurzel einer beliebigen Zahl mithilfe der linearen Suche bestimmen. 
Bitte implementieren Sie die Lösung als Guess-and-Check-Verfahren.

2) Bitte adaptieren Sie den Code für die Quadratwurzel- und Kubikwurzel-Suche derart, 
dass die Lösung nicht auf ganzzahlige Werte als Lösung beschränkt ist. Bitte stellen 
Sie sicher, dass dass die Kubikwurzel auch weiterhin für negative Werte bestimmt werden kann!
"""

x = float(input("Bitte einen Wert eingeben: "))

ans = 0.0
stepSize = 0.0001

while ans**3 < abs(x):
    ans = ans + stepSize

if(x<0):
    ans = -ans

print("Kubikwurzel von " + str(x) + " ist (annäherungsweise) " + f"{ans:>.2f}")
print("Gegenprobe: " + str(ans) + "³ = " + f"{ans**3:>.2f}")
