def substring(string, index=0, aktuell_substring="", dickster_substring=""):

    if index == len(string):
        return dickster_substring

    if index == 0 or string[index] >= string[index - 1]:
        aktuell_substring += string[index]
    else:
        aktuell_substring = string[index]

    if len(aktuell_substring) > len(dickster_substring):
        dickster_substring = aktuell_substring

    # Rekursiver Aufruf mit der nächsten Position
    return substring(string, index + 1, aktuell_substring, dickster_substring)

print(substring("hstmeanstuasmeanshst"))