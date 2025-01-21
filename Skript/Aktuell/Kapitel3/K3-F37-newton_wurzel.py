# Abbruchkriterium
epsilon = 0.01

# Suche Wurzel zu eingabeWert
eingabeWert = 24.0

# Grober Schaetzwert
schaetzung = eingabeWert/2

anzahlSchaetzungen = 0

while abs(schaetzung*schaetzung - eingabeWert) >= epsilon:
   anzahlSchaetzungen += 1
   schaetzung = schaetzung - (((schaetzung**2) - eingabeWert)/(2*schaetzung))
   
print('Anzal Schaetzungen= ' + str(anzahlSchaetzungen))
print('Quadratwurzel aus ' + str(eingabeWert) + ' ist annäherungsweise ' + str(schaetzung))