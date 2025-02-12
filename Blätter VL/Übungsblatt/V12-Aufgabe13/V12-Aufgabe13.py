class Bibliothek:
    def __init__(self):
        pass

class Nutzer:
    def __init__(self):
        pass
    

class Regal:
    def __init__(self,kapazität,id):
        self.kapazität = kapazität
        self.id = id
        self.medien = []

    def buch_einstellen(self,buch):
        self.medien.append(buch)

    def buch_ansehen(self,buch_id):
        return
    

class Medien:
    def __init__(self,id,titel,jahr,preis):
        self.id = id
        self.titel = titel
        self.jahr = jahr
        self.preis = preis
        
class Bücher(Medien):
    def __init__(self, id, titel, jahr, preis):
        super().__init__(id, titel, jahr, preis)
        

class DVD(Medien):
    def __init__(self, id, titel, jahr, preis):
        super().__init__(id, titel, jahr, preis)
    

class Zeitschrift(Medien):
    def __init__(self, id, titel, jahr, preis):
        super().__init__(id, titel, jahr, preis)
        