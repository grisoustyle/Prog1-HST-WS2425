print("Vorgabe")
iteration = 0
zahler = 0

while iteration < 5:
    for zeichen in "hallo, welt":
        zahler+=1        #hallo welt = 11, geht 5mal durch. Insgesamt also 5* jeweils +11
    print (f"Iteration Nr. {iteration}. Zahler ist {zahler}")
    iteration +=1
    
print("\nVariante 1")
'''
for iteration in range(5):
    zahler = 0
    while True:  #Nie aufhörende Schleife!! Kein Break!!
        for zeichen in "hallo, welt":
            zahler+=1
        print (f"Iteration Nr. {iteration}. Zahler ist {zahler}")
'''
print("Ich bin eine unendliche Schleife >:(")
print("Variante 1 != Vorgabe!")


print("\nVariante 2")
for iteration in range(5): #iteration wird immer um 1 erhöht bis 5
    zahler = 0 #zahler wird jedes mal auf 0 resettet
    while True:
        for zeichen in "hallo, welt":
            zahler +=1
        print (f"Iteration Nr. {iteration}. Zahler ist {zahler}")
        break
print("Variante 2 != Vorgabe!")

print("\nVariante 3")
zahler =0
text="hallo, welt"
for iteration in range(5):
    index=0 #index wird resettet, zahler nicht
    while index <len(text):
        zahler+=1
        index+=1
    print (f"Iteration Nr. {iteration}. Zahler ist {zahler}")
print("Variante 3 = Vorgabe!")

print("\nVariante 4")
zahler =0
text="hallo, welt"
for iteration in range(5):
    while True:
        zahler+=len(text) #zahler +11, 5mal (range 5)
        break
    print (f"Iteration Nr. {iteration}. Zahler ist {zahler}")
print("Variante 4 = Vorgabe!")

print("\nVariante 5")
zahler =0
text="hallo, welt"
for iteration in range (5):
    zahler+=len(text)
    print (f"Iteration Nr. {iteration}. Zahler ist {zahler}")
print("Variante 5 = Vorgabe!")