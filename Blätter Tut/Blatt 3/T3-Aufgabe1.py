#1
buchstabe= str(input("Buchstabe angeben: "))
zahler = 0

for zeichen in "bee":
    if buchstabe == zeichen:
        zahler+=1
print (f"Buchstabe {buchstabe} kommt {zahler}-mal im String vor.")