Liste = [4,5,6,7,8,9,10,11,12]

berechnung = (Liste[1]+Liste[4])
print(berechnung)

Liste.append(berechnung)
print(Liste)

del Liste[5]
print(Liste)