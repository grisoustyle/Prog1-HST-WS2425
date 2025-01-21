import math

def flaeche(radius):
    return (radius**2)*math.pi

def umfang(radius):
    return 2*radius*math.pi

def oberflaeche(radius):
    return (4*flaeche(radius))

def volumen(radius):
    return (4/3)*math.pi*(radius**3)