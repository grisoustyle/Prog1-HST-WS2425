x = float(input("Bitte einen Wert eingeben: "))

ans = 0.0
stepSize = 0.0001

while ans**3 < abs(x):
    ans = ans + stepSize

if(x<0):
    ans = -ans

print("Kubikwurzel von " + str(x) + " ist (annäherungsweise) " + f"{ans:>.2f}")
print("Gegenprobe: " + str(x) + "³ = " + f"{ans**3:>.2f}")