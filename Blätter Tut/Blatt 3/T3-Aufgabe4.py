#4
import random
geraten = ""
wahrezahl = random.randint(1,9)
while geraten != wahrezahl:
    geraten = int(input("Geben Sie eine Glückszahl an: "))
    #print (wahrezahl)
print(f"Die Zufallszahl war: {wahrezahl}")

#4a
geraten = ""
wahrezahl = random.randint(1,9)
rateversuch = 1
while rateversuch <=3:
    geraten = int(input("Geben Sie eine Glückszahl an: "))
    rateversuch+=1
    if geraten == wahrezahl:
        print(f"Die Zufallszahl war: {wahrezahl}")
        break
if geraten != wahrezahl:
    print("Keine Rateversuche mehr übrig!")
    print(f"Die Zufallszahl war: {wahrezahl}")