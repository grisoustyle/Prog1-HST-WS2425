def mul(a,b):
    if b==0:
        return 0
    elif b ==1:
        return a
    return a+mul(a,b-1)

print(mul(3,2))