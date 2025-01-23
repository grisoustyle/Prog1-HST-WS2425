def palindromcheck(wort):
    if wort == "":
        return True
    if len(wort)%2!=0:
        return False
    if wort[0] == wort[-1]:
        return True and palindromcheck(wort[1:-1])
    else:
        return False


'''wort = "test"
print(wort[0],wort[-1])
print(wort[1:-1])'''

print(palindromcheck("lagerregal"))