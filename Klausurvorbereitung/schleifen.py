def summe():
    summe = 0
    counter = 0

    while summe < 100:
        eingabe = int(input("Zahl eingeben: " ))
        counter +=1
        summe += eingabe
    return print(f"Summe: {summe}, Anzahl der Eingaben: {counter}")

def fizz_buzz():
    for zahl in range (1,100+1):
        if (zahl%3) == 0 and (zahl%5) == 0:
            print("FizzBuzz")
        elif (zahl%3) == 0:
            print("Fizz")
        elif (zahl%5) == 0:
            print("Buzz")
        else:
            print(zahl)

def sternchen(n):
    for zeile in range(1,n+1):
        print("*"*zeile)

def summe2(n):
    ergebnis = 0
    for zahl in range(0,n+1,2):
        ergebnis+=zahl
    return ergebnis

def list_filter(liste):
    neue_liste =[]
    for element in liste:
        if element%2==0:
            neue_liste.append(element)
    return neue_liste

print(list_filter([1, 2, 3, 4, 5, 6]))