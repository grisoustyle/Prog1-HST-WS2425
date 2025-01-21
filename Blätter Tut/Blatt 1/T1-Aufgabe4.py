#A4
#NAND
def NAND(boolA,boolB):
    return not(boolA and boolB)

#NOR
def NOR(boolA,boolB):
    return not(boolA or boolB)

#XNOR
def XNOR(boolA,boolB):
    return not((not(boolA and boolB) and (boolA or boolB)))

#tester
def wahrheitstabelle(Logikgatter,Gattername):
    print(Gattername,":")
    for boolA in [False, True]:
        for boolB in [False,True]:
            ergebnis = Logikgatter(boolA,boolB)
            print(boolA,boolB," = ",ergebnis)

wahrheitstabelle(NAND,"NAND")
wahrheitstabelle(NOR,"NOR")
wahrheitstabelle(XNOR,"XNOR")