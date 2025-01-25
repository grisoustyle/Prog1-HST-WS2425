def stern(breite):
    try:
        if breite < 5:
            raise Exception ("Mindestbreite unterschritten")
        if breite%2 == 0:
            raise Exception ("Breite muss ungerade Zahl sein!")
        
        breitenkopie = breite

        for i in range(0,breite//2):
            mitte = breite//2
            print(i*" " + "X" + (mitte-1)*" " + "X" + (mitte-1)*" "+"X")
            breite -=2

        print(breitenkopie*"X")

        for i in range(breitenkopie//2-1,-1,-1):
            mitte = breitenkopie//2
            print(i*" " + "X" + (mitte-1)*" " + "X" + (mitte-1)*" "+"X")
            breitenkopie +=2

    except Exception as ex:
        print(ex)

#print(7//2)
stern(9)


'''breite = breitenkopie
for i in range(breite // 2 -1, -1, -1):
    #print(i)
    mitte = breite // 2
    #print(f"mitte{mitte}")
    print(i * " " + "X" + (mitte - 3) * " " + "X" + (mitte - 3) * " " + "X")
    breite += 2'''