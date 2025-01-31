
def summe(n):
    summe = 0
    for i in range (1,n+1,2):
        #if i%2!=0:
        summe+=i
    return summe

print(summe(11))