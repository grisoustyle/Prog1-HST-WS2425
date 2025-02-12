def pot(a,b):
    if b <= 0:
        return 1
    return a*pot(a,b-1)

print(pot(2,3))