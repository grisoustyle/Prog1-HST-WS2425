class Tee:

    def __init__(self,name,klassifikation,verkaufspreis,aufgusstemperatur,ziehdauer,herkunftsland):
        self.__name = name
        self.__klassifikation = klassifikation
        self.__verkaufspreis = verkaufspreis
        self.__aufgusstemperatur = aufgusstemperatur
        self.__ziehdauer = ziehdauer
        self.__herkunftsland = herkunftsland

    def set_name(self,neu_name):
        self.__name = neu_name

    def get_name(self):
        return self.__name
    
    def set_klassifikation(self,neu_klassi):
        self.__klassifikation = neu_klassi

    def get_klassifikation(self):
        return self.__klassifikation
    
    def set_verkaufspreis(self,neu_preis):
        self.__verkaufspreis = neu_preis

    def get_verkaufspreis(self):
        return self.__verkaufspreis
    
    def set_aufgusstemperatur(self,neu_temp):
        self.__aufgusstemperatur = neu_temp

    def get_aufgusstemperatur(self):
        return self.__aufgusstemperatur
    
    def set_ziehdauer(self,neu_dauer):
        self.__ziehdauer = neu_dauer

    def get_ziehdauer(self):
        return self.__ziehdauer
    
    def set_herkunftsland(self,neu_land):
        self.__herkunftsland = neu_land

    def get_herkunftsland(self):
        return self.__herkunftsland
    
    def print_tee(self):
        print(self.__name,self.__klassifikation,self.__verkaufspreis,self.__aufgusstemperatur,self.__ziehdauer,self.__herkunftsland)


tees = [
    (Tee("Assam", "Schwarz", 7.80, 100, 3, "Indien")),
    (Tee("Ostfriesischer Tee", "Schwarz", 5.90, 100, 5, "Indien")),
    (Tee("Sencha", "Grün", 8.40, 90, 1, "Japan")),
    (Tee("Seogwang Sencha", "Grün", 15.40, 80, 2, "Südkorea")),
    (Tee("Java Barisan", "Oolong", 12.50, 90, 2, "Indonesien")),
    (Tee("Kaminfeuer", "Früchte", 4.50, 100, 10, "Deutschland"))
]

for item in tees:
    Tee.print_tee(item)

tees[1].set_herkunftsland("Deutschland")
tees[4].set_verkaufspreis(15.99)

tees[0].__name = "test" #macht nichts, weil private variable!

print("-----")

for item in tees:
    Tee.print_tee(item)
