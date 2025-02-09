def fakultät(n):
    if n == 0:
        return 1
    else:
        return n * fakultät(n-1)
    

print(fakultät(6))