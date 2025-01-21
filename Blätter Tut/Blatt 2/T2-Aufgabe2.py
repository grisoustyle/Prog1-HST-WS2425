zahl =int(input("Bitte geben Sie eine Zahl an: "))
counter = 0

if zahl <= 0:
    print(1)
else:
    while zahl > 0:
        zahl = zahl // 10
        counter = counter+1

print (f"Die Zahl hat {counter} Stellen.")