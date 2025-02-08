class Reisebüro:
    def __init__(self):
        self.reisen = []
    
    def reise_hizufügen(self,reise):
        self.reisen.append(reise)

class Reise:
    def __init__(self,id,ziel,preis):
        self.id = id
        self.ziel = ziel
        self.preis = preis

class Party(Reise):
    def __init__(self, id, ziel, preis):
        super().__init__(id, ziel, preis)

class Kultur(Reise):
    def __init__(self, id, ziel, preis):
        super().__init__(id, ziel, preis)

class Fahrrad(Reise):
    def __init__(self, id, ziel, preis):
        super().__init__(id, ziel, preis)

class Person:
    def __init__(self,name,id,tel):
        self.name = name
        self.id = id
        self.tel = tel

class Kunde(Person):
    def __init__(self, name, id, tel):
        super().__init__(name, id, tel)

class Mitarbeiter(Person):
    def __init__(self, name, id, tel,gehalt):
        super().__init__(name, id, tel)
        self.gehalt = gehalt

class Buchung:
    def __init__(self,start,end,preis,ziel):
        self.start = start
        self.end = end
        self.preis = preis
        self.ziel = ziel