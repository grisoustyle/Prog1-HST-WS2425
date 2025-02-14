def haus(breite,höhe):
    for i in range(1,breite+1,2):
        print(((breite-i)//2*" ")+i*"X")

    for i in range((höhe-1)-2): #-1 weil eine layer davon schon dach; -2 wegen tür
        print("X" * breite)

        
    print("X"+"  "+ (breite-3)*"X")
    print("X"+"  "+ (breite-3)*"X")  

haus(7,5)