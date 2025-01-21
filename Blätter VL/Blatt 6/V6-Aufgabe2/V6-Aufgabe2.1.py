#f(x)= x^3 -2x + 3x -5
#f'(x)= 3x^2 -2 + 3 

epsilon = 0.01

unteresLimit = 0
oberesLimit = 2
#Nullstelle liegt in [0;2]

schaetzung = unteresLimit + (oberesLimit - unteresLimit)/2.0

durchlauf = 0

#Nullstelle
nullstelle = 0

formel = (schaetzung**3 -2*schaetzung + 3*schaetzung -5)

while abs(formel-nullstelle) >= epsilon:

    if formel < nullstelle:
        unteresLimit = schaetzung
    else:
        oberesLimit = schaetzung
    durchlauf +=1

    print(f"Durchlauf {durchlauf}, Näherung {schaetzung}")

    schaetzung = unteresLimit + (oberesLimit - unteresLimit)/2.0
    formel = (schaetzung**3 -2*schaetzung + 3*schaetzung -5)

print (f"\nDie Nullstelle liegt näherungsweise bei {schaetzung}.\nAnzahl Durchläufe: {durchlauf}.\n")