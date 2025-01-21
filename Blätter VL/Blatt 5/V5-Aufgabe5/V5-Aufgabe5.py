# Damit der Code funktioniert, bitte auf der Kommandozeile ein Mal 
# folgenden Befehl eingeben: python3 -m pip install matplotlib 
import matplotlib.pyplot as plt 
import numpy as np 
import random 
 
# Die Funktion wertQuadratischeFunktion gibt den Wert der 
# Quadratischen Funktion der Form f(x) = ax^2 + bx + c zurück 
def wertQuadratischeFunktion(x, a, b, c): 
    return a * x**2 + b * x + c 
 
# Die Funktion ableitungQuadratischeFunktion gibt die Ableitung an x zurück 
def ableitungQuadratischeFunktion(x): 
    ''' 
    x: Position 
    returns: Wert der Ableitung an Position x 
    ''' 
    return 2 * a * x + b 
 
# Helfer-Funktion zur visuellen Ausgabe des Ergebnisses 
def plotQuadratischeFunktion(minimumQuadratischeFunktion , a, b, c): 
    x = np.linspace(-10, 10, 100) 
    y = wertQuadratischeFunktion(x, a, b, c) 
    plt.plot(x, y) 
    plt.plot(minimumQuadratischeFunktion,  
             wertQuadratischeFunktion(minimumQuadratischeFunktion, a, b, c),  
             marker="x", markersize=10,markerfacecolor="blue") 
    plt.show() 
 
# erzeuge eine zufällige Quadratische Funktion der Form 
# f(x) = ax^2 + bx + c 
a = random.uniform(0.5, 1.0) 
b = random.uniform(-5, 5) 
c = random.uniform(-5, 5) 
 
# Start des Programms 
print("Finde das Minimum der Quadratischen Funktion f(x)=" +  
      str(f"{a:.2f}") + "x²" + str(f"{b:+.2f}") + "x" + 
      str(f"{c:+.2f}") + " im Intervall [-10,10]") 
 


# Ihr Code kommt hier – !!! Hier entgegengesetzt der Aufgabenstellung mit binärer Suche anstatt linear !!!
obereslimit = 10
untereslimit = -10
x=0

while (2*a*x+b)!=0:
    mitte = (untereslimit+obereslimit)/2
    x= mitte

    if 2*a*x+b<0:
        untereslimit = mitte
    elif 2*a*x+b==0:
        break
    elif 2*a*x+b>0:
        obereslimit=mitte

# Variable minimumQuadratischeFunktion ablegen: 
minimumQuadratischeFunktion = x 
 

 
# Ausgabe Ihres angenäherten Ergebnisses 
print("Angenähertes Ergebnis: " + str(f"{minimumQuadratischeFunktion:.2f}")) 
# Ausgabe des mathematisch ermittelten Ergebnis zum Vergleich 
print("Zum Testen: Mathematisch korrektes Ergebnis: " + str(f"{-b/(2*a):.2f}")) 
# Visuelle Ausgabe des Ergebnisses   
plotQuadratischeFunktion(minimumQuadratischeFunktion, a, b, c)