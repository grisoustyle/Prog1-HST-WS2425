def fib (n): #0, 1, 1, 2, 3, 5, 8, 13, …
    print(f"\n---- Durchlauf mit fib({n})")
    if n == 0:
        print(f"Basisfall: fib(0) = 0")
        return 0
    elif n == 1 :
        print(f"Basisfall: fib(1) = 1")
        return 1
    else:
        print(f"Berechne: fib({n}) = fib({n-1}) + fib({n-2})")
        return fib(n-1) + fib(n-2)

stelle = int(input("n-te Stelle für fib eingeben: "))

print(f"\nZahl an {stelle}-ter Stelle: {(fib(stelle))}")