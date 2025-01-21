def anz_vokale(str):
    vokale = 0
    for zeichen in str:
        if zeichen in ["a","e","i","o","u"]:
            vokale +=1
    return vokale


#print(anz_vokale("hstmeanstuasmeanshst"))

def zeichen_alphabetisch(str):
    liste = []
    for zeichen in str:
        if zeichen not in liste:
            liste.append(zeichen)
    return sorted(liste)

#print(zeichen_alphabetisch("hstmeanstuasmeanshst"))

def laengster_alph_substring(str):
    substring = ""
    stelle = 0
    if str[stelle]>=str[stelle+1]:
        substring += str[stelle]
