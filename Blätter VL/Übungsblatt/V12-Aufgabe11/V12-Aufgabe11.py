

def potenz(basis,exponent):
    if exponent == 0:
        return 1
    elif exponent >=1:
        return basis * potenz(basis,exponent-1)
    
print(potenz(2,3))