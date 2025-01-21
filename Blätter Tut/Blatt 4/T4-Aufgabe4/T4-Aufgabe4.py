def nummerierte_argumente(*args):
    for index, argument in enumerate(args, start=1):
        print(f"{index}. {argument}")


#beispiele:
nummerierte_argumente("Apfel", "Banane", "Kirsche")
print("\n")
nummerierte_argumente(42, "Python", 3.14, True)
