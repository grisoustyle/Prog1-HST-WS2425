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


#rechteck(10)

def alternierendes_quadrat(breite):
    zähler = 0
    for y in range(breite):
        zeilenstr = ""
        for x in range(breite):
            abstand = min(x, y, breite - x - 1, breite - y - 1)
            zeilenstr += 'X' if abstand % 2 else ' '
        print(zeilenstr)

#alternierendes_quadrat(11)


def quadrat(breite):
    for y in range(breite):
        zeile = ""
        for x in range (breite):
            if (x==0)or (x==breite-1) or (y==0) or (y==breite-1) or ((x%2==0) and (y%2==0)):
                zeile+="X"
            else:
                zeile+=" "
        print(zeile)
    return

quadrat(19)