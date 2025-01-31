def stern(breite):
    try:
        if breite < 5:
            raise Exception ("Mindestbreite unterschritten")
        if breite%2 == 0:
            raise Exception ("Breite muss ungerade Zahl sein!")
        zähler = 1
        for y in range(breite):
            zeilenstr =""
            for x in range(breite):
                if (x==y) or ((x+y)==breite-1) or (x==breite//2) or (y==breite//2):
                    zeilenstr+=str(zähler)
                    zähler = (zähler+1)%10

                else:
                    zeilenstr+=" "
            print(zeilenstr)

    except Exception as ex:
        print(ex)

#print(7//2)
stern(9)