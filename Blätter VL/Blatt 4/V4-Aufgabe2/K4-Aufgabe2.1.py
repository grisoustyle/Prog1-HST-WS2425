def vokale(string):
    anzahl = 0
    for zeichen in string:
        if zeichen in ["a","e","i","o","u"]:
            anzahl +=1
    return anzahl

#print(vokale("hstmeanstuasmeanshst"))

def vokale_rek(string,zähler=0,startindex=0):

    if startindex >= len(string):
        return zähler
    
    if string[startindex] in ["a","e","i","o","u"]:
        zähler += 1
    
    return(vokale_rek(string,zähler,startindex+1))

print(vokale_rek("hstmeanstuasmeanshst"))
