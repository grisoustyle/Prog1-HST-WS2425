def palindrom(wort):
    if len(wort)<=1:
        return True
    elif wort[0]==wort[-1]:
        return palindrom(wort[1:-1])
    else:
        return False
    

print(palindrom("retsinakanister"))