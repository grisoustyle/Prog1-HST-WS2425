x = float(input('Bitte Dezimalzahl zwischen 0 und 1 eingeben: '))
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

print(f"Die Binärdarstellung der Dezimalzahl {x} lautet {result}")
