def ausgabe_bewegung(von,nach):
    print(f"{von} nach {nach}")

def turm(platten,von,nach,puffer):
    if platten == 1:
        ausgabe_bewegung(von,nach)
    else:
        turm(platten-1,von,puffer,nach)
        turm(1,von,nach,puffer)
        turm(platten-1,puffer,nach,von)

turm(4,1,2,3)