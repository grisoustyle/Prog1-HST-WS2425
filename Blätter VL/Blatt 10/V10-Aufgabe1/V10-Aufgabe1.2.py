class Tierheim:
    def __init__(self,name,tiere,räume):
        self.__name = name
        self.__tiere = []
        self.__räume = []

        self.__räume.append(Käfig("Hundezwinger",10))
        self.__räume.append(Voliere("Vogelkäfig",2))
        self.__räume.append(Aquarium("Wassertank",5))

    def add_tier(self,tier):
        self.__tiere.append(Tier)

    def del_tier(self):
        self.__tiere.remove(Tier)

class Raum:
    def __init__(self,bezeichnung,kapazität):
        self.__bezeichnung = bezeichnung
        self.__kapazität = kapazität

class Voliere(Raum):
    pass
class Käfig(Raum):
    pass
class Aquarium(Raum):
    pass

class Tier:
    def __init__(self,name,futter,raum):
        self.__name = name
        self.__futter = futter
        self.__raum = Raum(raum)

class Hund(Tier):
    def __init__(self, name, futter, raum, rasse):
        super().__init__(name, futter, raum)
        self.rasse = rasse
    
class Vogel(Tier):
    def __init__(self, name, futter, raum, ordnung):
        super().__init__(name, futter, raum)
        self.ordnung = ordnung
    
class Fisch(Tier):
    def __init__(self, name, futter, raum, wassertyp):
        super().__init__(name, futter, raum)
        self.wassertyp = wassertyp
    

Tierheim.add_tier("Bello","Fleisch",0,"Retriever")