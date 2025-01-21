#f(x)= x^3 -2x + 3x -5
#f'(x)= 3x^2 -2 + 3 

epsilon = 0.01

#Startwert 2
schaetzung = 2

durchlauf = 0

#Nullstelle
nullstelle = 0

formel = (schaetzung**3 -2*schaetzung + 3*schaetzung -5)
ableitung = (3*schaetzung**2)-2+3

while abs((formel - nullstelle)) >= epsilon: #für x wird schaezung(=aktueller Wert) eingesetzt
    formel = (schaetzung**3 -2*schaetzung + 3*schaetzung -5)
    ableitung = (3*schaetzung**2)-2+3

    schaetzung = schaetzung - formel/ableitung
    durchlauf +=1

    print(f"Durchlauf {durchlauf}, Näherung {schaetzung}")
    
print (f"\nDie Nulstelle liegt näherungsweise bei {schaetzung}.\nAnzahl Durchläufe: {durchlauf}.\n")