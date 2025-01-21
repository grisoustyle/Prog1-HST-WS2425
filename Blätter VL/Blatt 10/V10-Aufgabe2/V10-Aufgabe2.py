class Artikel:
    def __init__(self,bezeichnung,preis):
        self.bezeichnung = bezeichnung
        self.preis = preis

class Person:
   def __init__(self):
       pass

class Mitarbeiter(Person):
    pass

class Kunde(Person):
    def __init__(self, name, adresse):
        super().__init__(name, adresse)

    def bestellung_aufgeben(self):
        return Bestellung(self)

    
class Bestellung:
    def __init__(self,kunde):
        self.kunde = kunde
        self.artikel = []
        self.mitarbeiter = []



'''Ein  Webshop  verkauft  über  das  Internet  Artikel. 
Artikel  haben  eine  Bezeichnung  und  einen  Preis.
Kunden  können  Bestellungen  aufgeben.
Kunden  haben  einen  Namen  und eine Adresse.
Eine Bestellung enthält einen oder mehrere Artikel bzw. jeder Artikel kann  auf verschiedenen Bestellungen erscheinen.
Eine Bestellung wird von einem oder mehreren Mitarbeitern bearbeitet. Sowohl Mitarbeiter als auch Kunden sind Personen.'''