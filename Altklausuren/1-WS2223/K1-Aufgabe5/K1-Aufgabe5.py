# a b c d e f g h i j k l m n o p q r s t u v w x y z
alphabetstr = "abcdefghijklmnopqrstuvwxyz"

'''alphabet = {

}
index = 0
for letter in alphabetstr:
    index +=1
    alphabet[letter]= index

print(alphabet)'''

def codieren(wort,shift):
    verschlüsselt = ""
    for buchstabe in wort: #t
            
        alt_index = alphabetstr.index(buchstabe)
        #print(f"altindex {alt_index}")
        neu_index = (alt_index+shift)%26
        #print(f"neuindex {neu_index}")
        verschlüsselt += alphabetstr[neu_index]
    print(verschlüsselt)

codieren("testwort",1)

