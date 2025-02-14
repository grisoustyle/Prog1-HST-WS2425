def haus(breite,höhe):
    try:
        if not(type(breite)==int and type(höhe)==int):
            raise Exception ("Nur Integer erlaubt!")
        if breite < 5 or höhe < 3 or breite%2==0:
            raise Exception ("Hausmaße ungültig!")
        
        #Dach
        for i in range(1, breite + 1, 2):   #range(startwert,endwert,schrittwert) 1 3 5
            print(" "*((breite-i)//2) + "*"*i) #_*((5-1)//2)= 2*_ + "*"*1;   _*(2//2)+"*"*3;   _*(0//2)+"*"*5

        #Wand
        for i in range((höhe-1)-2): #-1 weil eine layer davon schon dach; -2 wegen tür
            print("*" * breite)

        #Tür
        print("*"+"  "+ (breite-3)*"*")
        print("*"+"  "+ (breite-3)*"*")

    except Exception as ex:
        print(ex)

haus(5,3)
