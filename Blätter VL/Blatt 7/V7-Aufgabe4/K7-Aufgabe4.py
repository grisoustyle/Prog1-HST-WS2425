def mul(a,b):
    if b <= 0:
        return 0
    return a+mul(a,b-1)
    
print(mul(5,3))

def add(a,b):
    if b <= 0:
        return a
    return 1 + add(a,b-1)

print(add(5,3))
