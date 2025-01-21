#1a
def Aufgabe_a (name,alter,schule):
    print(f"{name}({alter}), besucht {schule}.")

Aufgabe_a(
    name=str(input("Name: ")),
    alter=str(input("Alter: ")),
    schule=str(input("Schule: "))
)
