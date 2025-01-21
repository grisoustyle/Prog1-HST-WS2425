def tannenbaum():
    try:
        breite = int(input("Breite eingeben: "))
        if breite < 5 or breite%2 ==0:
            raise Exception("Zahl muss >5 und ungerade sein!")
        else:
            sterne = 1
            begrenzung = breite//2

            while sterne <= breite:
                print(((begrenzung*" ") +sterne*"*"))
                begrenzung -=1
                sterne +=2
            print(((breite//2)-1)*" "+"***")

    except ValueError:
        print("Ungültige Eingabe! Nur Zahlen erlaubt!")
        tannenbaum()
    except Exception as ex: 
        print(ex)
        tannenbaum()

tannenbaum()


#_ _ *
#_ * * *
#* * * * *
#_ * * *