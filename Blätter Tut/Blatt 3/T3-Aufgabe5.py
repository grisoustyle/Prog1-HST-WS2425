#5
eingabe = str(input("Geben Sie ein Wort ein: "))
buchstabenzahl = 0
ziffernzahl = 0

for zeichen in eingabe:
    if zeichen.isalpha():
        buchstabenzahl+=1
    elif zeichen.isnumeric():
        ziffernzahl+=1
print(f"Anzahl Buchstaben: {buchstabenzahl}")
print(f"Anzahl Zahlen: {ziffernzahl}")
