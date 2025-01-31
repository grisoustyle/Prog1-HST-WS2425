def stern(breite):
    try:
        if breite < 5:
            raise Exception ("Mindestbreite unterschritten")
        if breite%2 == 0:
            raise Exception ("Breite muss ungerade Zahl sein!")
        
        mitte = breite // 2

        for i in range(mitte):
            print(' ' * i + 'X' + ' ' * (mitte - 1 - i) + 'X' + ' ' * (mitte - 1 - i) + 'X')

        print('X' * breite)

        for i in range(mitte):
            print(' ' * (mitte - 1 - i) + 'X' + ' ' * i + 'X' + ' ' * i + 'X')

    except Exception as ex:
        print(ex)

#print(7//2)
stern(9)