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

sternchen(3)