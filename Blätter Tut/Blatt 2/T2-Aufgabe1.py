'''
zahl = int(input("Zahl eingeben: "))
while zahl >=0:
    if zahl % 4 == 0 and zahl % 5 == 0:
        print("fizzbuzz")
        zahl = zahl-1
    elif zahl % 4 == 0:
        print("fizz")
        zahl = zahl-1
    elif zahl % 5 == 0:
        print("buzz")
        zahl = zahl-1
    else:
        print(zahl)
        zahl = zahl-1
        
'''

zahl = int(input("Zahl eingeben: "))
for i in range (1,zahl+1):
    if i % 4 == 0 and zahl % 5 == 0:
        print("fizzbuzz")
    elif i % 4 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)