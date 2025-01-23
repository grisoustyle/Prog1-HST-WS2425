def raute(breite):
    spacer = breite//2
    #print (f"spacer{spacer}")
    for i in range (1,breite+1,2):
        print((spacer*" ") + i*"X")
        spacer -=1
    spacer = 1
    for i in range(breite-2,0,-2):
        #print(i)
        print((spacer*" ") + i*"X")
        spacer +=1
        
raute(19)