def stern(breite):
    spacer = breite//2
    for i in range(1,breite+1,2):
        print((spacer*" ")+i*"X")
        spacer -=1
    spacer = 1
    for i in range(breite-2,0,-2):
        print((spacer*" ")+i*"X")
        spacer +=1

stern(9)

