def rechteck(breite):
    zähler = 0
    for y in range(0,breite+1):
        zeilenstr=""
        for x in range(0,breite+1):
            if y ==0 or x == 0 or x==breite or y==breite or x==breite//2 or y==breite//2:
                zeilenstr+=str(zähler)
                zähler = (zähler+1)%10
            else:
                zeilenstr+=" "

        print(zeilenstr)


rechteck(10)