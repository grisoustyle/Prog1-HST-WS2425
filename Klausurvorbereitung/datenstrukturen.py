def woerter_zaehlen(satz=""):
    wort_dic = {

    }

    wortliste = satz.split()
    
    for item in wortliste:
        if item in wort_dic:
            wort_dic[item] +=1
        else:
            wort_dic[item] = 1
    return wort_dic


#print(woerter_zaehlen("Hallo Welt Hallo ChatGPT"))
