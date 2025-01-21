intZahl = int(input("Zahl im Dezimalsystem eingeben: "))

zahl = intZahl

if zahl < 0:
   isNeg = True
   num = abs(zahl)

else:
   isNeg = False
result = ''

if zahl == 0:
   result = '0'
   
while zahl > 0:
   result = str(zahl%2) + result
   zahl = zahl//2

if isNeg:
   result = '-' + result

print (intZahl, "dargestellt als binäre Zahl ist", result)