def teilbar(n):
    teilbare = []
    for i in range (1,n+1):
        if i%5==0:
            teilbare.append(i)
    return teilbare

print(teilbar(20))