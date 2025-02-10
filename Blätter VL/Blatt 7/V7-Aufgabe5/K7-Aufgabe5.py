def potenz(x,n):
    if n == 0:
        return 1
    return x * potenz(x,n-1)

print(potenz(9,7))