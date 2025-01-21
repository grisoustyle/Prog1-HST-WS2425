#mit Userinput
def show_employee(name,gehalt):
    if gehalt == 0:
        gehalt = 450
    return name,gehalt

name,gehalt=show_employee(
    str(input("\nName eingeben: ")),
    int(input("Gehalt eingeben: "))
)

print(f"\nMitarbeiter {name} verdient {gehalt}€.\n")



#ohne Userinput
def show_employee(name,gehalt=450):
    print(f"\nMitarbeiter {name} verdient {gehalt}€.\n")

show_employee("Hans",6723)
show_employee("Klara")