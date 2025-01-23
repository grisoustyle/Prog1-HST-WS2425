def palindromcheck(wort):
    wort = wort.lower()

    if len(wort)<=1:
        return True
    if wort[0] == wort[-1]:
        return palindromcheck(wort[1:-1])
    else:
        return False


'''wort = "test"
print(wort[0],wort[-1])
print(wort[1:-1])'''

print(palindromcheck("LageRregal"))
print(palindromcheck("Reliefpfeiler"))