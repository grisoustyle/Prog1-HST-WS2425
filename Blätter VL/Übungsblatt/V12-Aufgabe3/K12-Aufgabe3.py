def teiler(n):
    zahlen = []
    for zahl in range (1,n+1):
        if zahl%5==0:
            zahlen.append(zahl)
    return print(f"Natürliche Zahlen zwischen 1 und {n} die restlos durch 5 teilbar sind: {zahlen}")

teiler(20)