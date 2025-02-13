def add(a,b):
    if b <=0:
        return a
    return add(a+1,b-1)

print(add(3,5))

def sum(n):
    if n <= 1:
        return 1
    return n+(sum(n-1))

print(sum(5))

def sub(a,b):
    if b <=0:
        return a
    return sub(a-1,b-1)

print(sub(5,3))