#bzw V6-A4
def umrechnung(x):
   
    p = 0

    while((2**p)*x)%1!= 0:
        print(f"{p} Rest: {(2**p)*x-int((2**p)*x)}")
        p+= 1

    num = int(x*(2**p))

    result = ''
    if num == 0:
        result = '0'

    while num > 0:
        result = str(num%2) + result
        num = num//2

    for i in range(p-len(result)):
        result = '0'+ result

    result = result[0:-p] + '.' + result[-p:]
    return result

def truncate(input_str,prec): #schneidet str ab
    return input_str[:(prec+1)]

def umrechnung(str_wert):
    value = 0.0
    exp = -1

    for pos in range(1,len(str_wert)):
        if str_wert[pos] == "1":
            value += 2**exp
        exp -=1
    return value


x = float(input('Bitte Dezimalzahl zwischen 0 und 1 eingeben: '))

erg1 = umrechnung(x)
print(f"\nDie Binärdarstellung der Dezimalzahl {x} lautet.\n{erg1}")

prec=int(input("\nWie viele Nachkommastellen: "))
erg2 = truncate(erg1,prec)
print(f"\nDie Binärdarstellung der Dezimalzahl {x} mit {prec} Nachkommastellen lautet:\n{erg2}")

erg3 = (umrechnung(erg2))
print(erg3)