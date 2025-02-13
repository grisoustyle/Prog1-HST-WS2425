from aufgabe03 import entferne_sonderzeichen

'''def textanalyse(satz):
    satz = satz.lower()
    wort =""
    dic={}
    for zeichen in satz:
        if zeichen not in "?!.,:; ":
            wort+=zeichen
        else:
            if wort not in dic:
                dic[wort]=1
                wort =""
            else:
                dic[wort]+=1
                wort=""
    return dic

print(textanalyse("Das ist ein Test. Das ist nur ein Test. Apfelkuchen ist lecker!"))'''

satz=(entferne_sonderzeichen("Das ist ein Test. Das ist nur ein Test. Apfelkuchen ist lecker!"))

def textanalyse2(satz):
    satz = satz.split(" ")
    dic ={}
    for wort in satz:
        if wort not in dic:
            dic[wort]=1
        else:
            dic[wort]+=1

    for wort in dic:
        print(f"{wort} - {dic[wort]}")
    return 

(textanalyse2(satz))