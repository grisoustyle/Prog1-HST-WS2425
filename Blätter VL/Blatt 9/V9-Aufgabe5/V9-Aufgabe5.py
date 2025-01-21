class Auto:
    def __init__(self,marke,modell,baujahr,farbe):
        self.__marke = marke
        self._modell = modell
        self._baujahr = baujahr
        self._farbe = farbe

    def set_marke(self,neu_marke):
        self.__marke = neu_marke

    def get_marke(self):
        return self.__marke
    
    def set_modell(self,neu_modell):
        self._modell = neu_modell

    def get_modell(self):
        return self._modell
    
    def set_baujahr(self,neu_baujahr):
        self._baujahr = neu_baujahr

    def get_baujahr(self):
        return self._baujahr
    
    def set_farbe(self,neu_farbe):
        self._farbe = neu_farbe

    def get_farbe(self):
        return self._farbe
    
    def print_auto(self):
        print(self.__marke,self._modell,self._baujahr,self._farbe)

autos = [
    (Auto("BMW", "5er", 2020, "Schwarz")),
    (Auto("Volvo", "V70", 2023, "Blau")),
    (Auto("Mercedes", "C-Klasse", 2002, "Silber")),
    (Auto("Ford", "Mustang", 1995, "Rot")),
    (Auto("Tesla", "Model S", 2021, "Weiß")),
    (Auto("VW", "Passat", 1900, "Silber"))
]

for items in autos:
    Auto.print_auto(items)


meinBMW = Auto("BMW", "5er", 2020, "Schwarz")
meinBMW.set_marke("Volvo")
meinBMW._farbe='lila'
meinBMW.__marke='Tesla'
meinBMW.print_auto()
meinBMW.set_marke("Bmw")
meinBMW.print_auto()

# name = Public
# _name = Protected
# __name = Private; unveränderbar, nur durch setter in Klasse
