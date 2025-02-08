def flaeche(k):
    return k**2

def umfang(k):
    return 4*k

def oberflaeche(k):
    return 4*flaeche(k)

def volumen(k):
    return k**3

k=int(input("Welche Kantenlänge hat das Quadrat bzw. der Würfel in cm? "))
print(f"Fläche Quadrat: {flaeche(k)}cm^2\nUmfang Quadrat: {umfang(k)}cm\nOberfläche Würfel: {oberflaeche(k)}cm^2\nVolumen: {volumen(k)}cm^3")