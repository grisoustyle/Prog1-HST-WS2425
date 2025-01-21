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
 
 
print("Finde die Position des Minimums des Polynoms f(x)=" + 
      str(f"{a:.2f}") + "x^4 - " + str(f"{b:.2f}") + "x" + str(f"{c:+.2f}") + 
      " im Intervall [-10,10]") 
 
# Ihr Code kommt hier – das Ergebnis bitte in der 
# Variable posMinimumPolynom ablegen und 
# die Anzahl benötigter Schritte in anzSchritte: 
epsilon=0.01
anzSchritte = 0 
schaetzung = 5 #random gewählt?? am besten innerhalb Intervall damit weniger Schritte; Allerdings hier nicht 0 da sonst teilen durch 0 in 27

while abs(ableitungPolynom(schaetzung)) >= epsilon:
    schaetzung= schaetzung - ableitungPolynom(schaetzung) / (12*a*schaetzung**2)
    anzSchritte +=1
    print (f"Schritt {anzSchritte}, Schätzung: {schaetzung}")

posMinimumPolynom = schaetzung 
 
print(f"Anzahl Schritte: {anzSchritte}") 
print(f"Angenähertes Ergebnis: {posMinimumPolynom:.2f}")
print(f"Zum Testen: Korrektes Ergebnis: {(b/(4*a))**(1/3):.2f}\n")