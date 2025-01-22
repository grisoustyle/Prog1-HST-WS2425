def hst_check(string,startindex=0,counter=0):
    if startindex > len(string):
        return counter

    if string[startindex:startindex+3] == "hst":
        counter+=1

    return hst_check(string,startindex+1,counter)

print(hst_check("hstmeanstuasmeanshsthsthhsstthst"))