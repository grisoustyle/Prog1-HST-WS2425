def geradeZahl(i):
    print(f"Wir testen die Zahl {i}")
    return i%2==0

i = int(input("Testzahl: "))
print(geradeZahl(i))


def justPrint():
    print("test")


def printAndReturn():
    print("test")
    return "test"

print(justPrint())
print(printAndReturn())