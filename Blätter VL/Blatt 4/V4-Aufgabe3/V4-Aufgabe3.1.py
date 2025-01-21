#Häuser auf der Kommandozeile
breite = int(input("Breite: "))
hohe = int(input("Höhe: "))

if breite < 5 or hohe < 3 or breite % 2 == 0:
    print("Unzulässiges Haus")

else:
    #Dach
    for i in range(1, breite + 1, 2):   #range(startwert,endwert,schrittwert) 1 3 5
        print(" "*((breite-i)//2) +"*"*i) #_*((5-1)//2)= 2*_ + "*"*1;   _*(2//2)+"*"*3;   _*(0//2)+"*"*5

    #Wand
    for i in range((hohe-1)-2): #-1 weil eine layer davon schon dach; -2 wegen tür
        print("*" * breite)

    #Tür
    print("*"+"  "+ (breite-3)*"*")
    print("*"+"  "+ (breite-3)*"*")