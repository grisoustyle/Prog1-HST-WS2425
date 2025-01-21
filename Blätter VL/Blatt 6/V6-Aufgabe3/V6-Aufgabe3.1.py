#f(x)= ax^4 − bx + c

import random 
 
a = random.uniform(0.5, 1.0) 
b = random.uniform(0, 1000) 
c = random.uniform(-1000, 1000) 
 
def ableitungPolynom(x): 
    ''' 
    x: Position 
    returns: Wert der Ableitung an Position x 
    ''' 
    return 4*a*x**3 - b 
 
 
print("\nFinde die Position des Minimums des Polynoms f(x)=" + 
      str(f"{a:.2f}") + "x^4 - " + str(f"{b:.2f}") + "x" + str(f"{c:+.2f}") + 
      " im Intervall [-10,10]") 
 
# Ihr Code kommt hier – das Ergebnis bitte in der 
# Variable posMinimumPolynom ablegen und 
# die Anzahl benötigter Schritte in anzSchritte: 
epsilon = 0.01

unteresLimit= -10
oberesLimit= 10

schaetzung = unteresLimit + (oberesLimit - unteresLimit)/2.0
anzSchritte = 0 

while abs(ableitungPolynom(schaetzung))>=epsilon:
    anzSchritte +=1
    if ableitungPolynom(schaetzung) > 0:
        oberesLimit = schaetzung
        print(f"Schritt {anzSchritte}, Bereich: [{unteresLimit};{oberesLimit}]")
    else:
        unteresLimit = schaetzung
        print(f"Schritt {anzSchritte}, Bereich: [{unteresLimit};{oberesLimit}]")

    schaetzung = unteresLimit + (oberesLimit - unteresLimit)/2.0  

posMinimumPolynom = schaetzung

 
print(f"Anzahl Schritte: {anzSchritte}") 
print(f"Angenähertes Ergebnis: {posMinimumPolynom:.2f}")
print(f"Zum Testen: Korrektes Ergebnis: {(b/(4*a))**(1/3):.2f}\n")