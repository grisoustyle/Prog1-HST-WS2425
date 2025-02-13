def stern(breite):
    for y in range(breite):
        zeile = ""
        for x in range(breite):
            if (x==y)or((x+y)==breite-1) or (x==breite//2) or (y==breite//2):
                zeile += "X"
            else:
                zeile += " "
        print(zeile)

stern(9)