# Abstrakte Klasse Person
class Person:
    def __init__(self, name, id, tel):
        self.name = name
        self.id = id
        self.tel = tel

# Mitarbeiter erbt von Person
class Mitarbeiter(Person):
    def __init__(self, name, id, tel, gehalt, dienstgrad):
        super().__init__(name, id, tel)
        self.gehalt = gehalt
        self.dienstgrad = dienstgrad

# Kunde erbt von Person
class Kunde(Person):
    def __init__(self, name, id, tel):
        super().__init__(name, id, tel)

    def leihen(self, fahrrad, start_zeitpunkt, end_zeitpunkt):
        return Leihe(self, fahrrad, start_zeitpunkt, end_zeitpunkt)

# Abstrakte Klasse Fahrrad
class Fahrrad:
    def __init__(self, nummer, groesse, marke, anschaffungspreis):
        self.nummer = nummer
        self.groesse = groesse
        self.marke = marke
        self.anschaffungspreis = anschaffungspreis

# Spezialisierungen von Fahrrad
class Rennrad(Fahrrad):
    def __init__(self, nummer, groesse, marke, anschaffungspreis, sport_tauglichkeit):
        super().__init__(nummer, groesse, marke, anschaffungspreis)
        self.sport_tauglichkeit = sport_tauglichkeit

class Mountainbike(Fahrrad):
    def __init__(self, nummer, groesse, marke, anschaffungspreis, federung):
        super().__init__(nummer, groesse, marke, anschaffungspreis)
        self.federung = federung

class Elektrorad(Fahrrad):
    def __init__(self, nummer, groesse, marke, anschaffungspreis, akku_kapazitaet):
        super().__init__(nummer, groesse, marke, anschaffungspreis)
        self.akku_kapazitaet = akku_kapazitaet

# Klasse Leihe
class Leihe:
    def __init__(self, kunde, fahrrad, start_zeitpunkt, end_zeitpunkt,preis):
        self.kunde = kunde
        self.fahrrad = fahrrad
        self.start_zeitpunkt = start_zeitpunkt
        self.end_zeitpunkt = end_zeitpunkt
        self.preis = preis