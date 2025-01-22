def dreieck_kreuz(breite):
    try:
        if breite%2==0:
            raise Exception ("Nur ungerade Breite zulässig!")
        if (type(breite)!=int):
            raise Exception ("Nur Integer erlaubt!")
        
        #Dreieck
        breite_punkte =0
        for i in range(breite):
            print((breite_punkte+i)*". " + "* "*(breite-i))

        #Kreuz
        

    except Exception as ex:
        print(ex)

dreieck_kreuz(7)

