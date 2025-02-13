def zahlenpyramide(höhe):
    zahl = 0
    for i in range(1,höhe+1):
        spacer =((höhe-i)*" ")
        zeile = []
        for zahl in range(zahl, zahl + i):
            zeile.append(str(zahl % 10))
        print(spacer+" ".join(zeile))

zahlenpyramide(20)