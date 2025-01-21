'''Schreiben Sie folgendes Programm mit einem iterativen Ansatz: (10 Punkte) 
 
Berechnen Sie die Summe der ersten n Fibonacci-Zahlen. Der Wert von n soll zunächst vom Nutzer 
abgefragt werden. Die Fibonacci-Zahlen sollen im Rahmen des Programms mit einem iterativen 
Verfahren bestimmt und ausgegeben werden. Abschließend soll die Summe der ersten n Fibonacci-
Zahlen berechnet und ausgegeben werden. 
 
Hilfestellung: Die Fibonacci-Zahlenfolge beginnt mit den Zahlen 0 und 1, und jede nachfolgende Zahl 
ist die Summe der beiden vorherigen Zahlen. Zum Beispiel sind die ersten fünf Fibonacci-Zahlen 0, 1, 
1, 2 und 3, und ihre Summe ist 7.'''

# 0 1 1 2 3 5 8

n = int(input("Wie viele Fibonacci-Zahlen sollen aufsummiert werden? "))
fib1 = 0
fib2 = 1
summe = 0

for zahl in range(n):
    print(fib1)
    summe += fib1
    fib1, fib2 = fib2, fib1 + fib2

print(f"Summe der ersten {n} Fibonacci-Zahlen: {summe}")

