def pascal(z,s):
    if s == 1 or s == z:
        return 1
    print(z,s)
    return pascal(z-1,s-1)+pascal(z-1,s)
