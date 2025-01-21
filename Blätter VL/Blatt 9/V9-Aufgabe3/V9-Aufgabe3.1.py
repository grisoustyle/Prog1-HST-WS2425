person = {

}

person["Name"]="Max"
person["Alter"]=30
person["Stadt"]="Berlin"

print(person["Name"],type(person["Name"]))

for item in person:
    print(person[item],type(person[item]))

person["Alter"]=35

print(person)

personen = [

]

personen.append(person)
personen.append(person.copy()) #muss kopie sein weil sollst auf dasselbe verweisen und ändern

print(personen)

personen[1]["Name"]= "Mirijam"
personen[1]["Alter"]=30

print(personen)