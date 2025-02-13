def anz_vokale(str):
    counter =0
    for buchstabe in str:
        if buchstabe in "aeiou":
            counter+=1
    return print(counter)

anz_vokale("hstmeanstuasmeanshst")

def zeichen_alphabetisch(str):
    sortiert = []
    for buchstabe in "abcdefghijklmnopqrstuvwxyz":
        for zeichen in str:
            if zeichen == buchstabe:
                if zeichen not in sortiert:
                    sortiert.append(zeichen)
    return print(sortiert)

zeichen_alphabetisch("hstmeanstuasmeanshst")

def laengster_alph_substring(str):
    return