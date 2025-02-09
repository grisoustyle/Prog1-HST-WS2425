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

anzSchritte = 0

def ableitung2(x):
    return 12*a*x**2
    
epsilon = 0.001
schätzung = 5

while abs(ableitungPolynom(schätzung))>=epsilon:
    schätzung = schätzung - ableitungPolynom(schätzung)/ableitung2(schätzung)
    anzSchritte +=1
    print (f"Schritt {anzSchritte}, Schätzung: {schätzung}")

posMinimumPolynom = schätzung
 
print("Anzahl Schritte: " + str(anzSchritte)) 
print("Angenähertes Ergebnis: " + str(f"{posMinimumPolynom:.2f}")) 
print("Zum Testen: Korrektes Ergebnis: " + str(f"{(b/(4*a))**(1/3):.2f}")) 
 