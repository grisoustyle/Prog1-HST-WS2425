class Bank:
    def __init__(self):
        pass

class Konten:
    def __init__(self,kontonr,kontostand):
        self.kontonummer = kontonr
        self.kontostand = kontostand

class Girokonto(Konten):
    def __init__(self, kontonr, kontostand,zinssatz):
        super().__init__(kontonr, kontostand)
        self.zinssatz = zinssatz

class Sparkonto(Konten):
    def __init__(self, kontonr, kontostand,zinssatz):
        super().__init__(kontonr, kontostand)
        self.zinssatz = zinssatz

class Kreditkonto(Konten):
    def __init__(self, kontonr, kontostand,zinssatz):
        super().__init__(kontonr, kontostand)
        self.zinssatz = zinssatz

class Dienstleistung:
    def __init__(self,bezeichnung):
        self.bezeichnung = bezeichnung

class Einzahlung(Dienstleistung):
    pass

class Auszahlung(Dienstleistung):
    pass

class Kunde:
    def __init__(self,name):
        self.name = name

class Mitarbeiter:
    def __init__(self,persnr,name):
        self.personalnummer = persnr
        self.name = name