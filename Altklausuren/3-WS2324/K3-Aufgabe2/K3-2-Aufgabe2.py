def fib(n):
    fib1 = 0
    fib2 = 1
    summe = 0
    for zahl in range(1,n+1):
        print(fib1)
        summe += fib1
        fib1,fib2=fib2,fib1+fib2
    return summe
n= int(input("Aufsummieren: "))
print(f"Summe der {n}-fib = {fib(n)}")