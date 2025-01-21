s = "hstmeanstuasmeanshst"

vokale ={"a", "e", "i", "o", "u"}

##1
print("\n2.1)")
anzahlvokale =0

for buchstabe in s: #durchläuft wort
    if buchstabe in vokale: 
        anzahlvokale +=1
print (f"Anzahl Vokale: {anzahlvokale}")

##2
print("\n2.2)")
ergebnis=""
for buchstabe in sorted(s): #macht aus string sortierte buchstabenliste
    if buchstabe not in ergebnis: #rauswurf doppelter buchstaben
            ergebnis+=buchstabe+" "
print(ergebnis)
#print (sorted(s))

ergebnis = ""
for buchstabe in "abcdefghijklmnopqrstuvwxyz": #geht reihe nach alphabet jeden buchstaben durch
    if buchstabe in s: #wenn es ein "a" in s gibt...
        ergebnis += buchstabe + " " #füg "a" 1mal zu ergebnis hinzu, dann mach weiter mit b
print(ergebnis)

##3
print("\n2.3)")
anzahlhst =0
for pos in range(len(s)-2): #-2 weil 3er pakete und sonst letzten 2 nur "st" und "t"
    print (s[pos : pos +3])
    if s[pos : pos +3] == "hst": #[pos:pos+3] erstellt substring start index und länge 3 für jeden buchstabendurchlauf; = "hst","stm","tme,..."
        anzahlhst +=1
print(f"Anzahl von hst in String: {anzahlhst}")
     
##4
print("\n2.4)")

pos = 0
lange_langster_ASubstring = 0
langster_ASubstring = ""

while pos < len(s):
    # extrahiere Substring bis Ende ab pos
    substring = s[pos:]
    alphabetischerAnfangInSubstring = substring[0]

    # starte mit dem nächsten Element
    positionInSubstring = 1
    while positionInSubstring < len(substring) and substring[positionInSubstring] >= substring[positionInSubstring - 1]:
        alphabetischerAnfangInSubstring += substring[positionInSubstring]
        positionInSubstring += 1

    # vergleiche mit global (bisher) längstem alphabetischem Substring
    if len(alphabetischerAnfangInSubstring) > lange_langster_ASubstring:
        lange_langster_ASubstring = len(alphabetischerAnfangInSubstring)
        langster_ASubstring = alphabetischerAnfangInSubstring

    pos += 1

print("Längster Substring in alphabetischer Reihenfolge: " + langster_ASubstring)