#ganzzahlige Werte:
x = int(input("Bitte einen ganzzahligen Wert eingeben: "))
ans = 0

while ans**2 < x:
    ans = ans + 1
if ans**2 != x:
    print(str(x) + " hat keine ganzzahlige Quadratwurzel!")
else:
    print("Quadratwurzel von " + str(x) + " ist " + str(ans))
    print("Gegenprobe: " + str(ans) + "² = " + str(ans**2))



#beliebige Zahlen:
x = float(input("Bitte einen Wert eingeben: "))
ans = 0.0
stepSize = 0.0001

while ans**2 < x:
    ans = ans + stepSize

print("Quadratwurzel von " + str(x) + " ist annäherungsweise " + f"{ans:>.2f}")
print("Gegenprobe: " + f"{ans:>.2f}" + "² = " + f"{ans**2:>.2f}")
