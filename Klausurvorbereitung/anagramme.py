def anagramm(wort1, wort2):
    if len(wort1) != len(wort2):
        return False

    wort2_liste = list(wort2)

    for buchstabe in wort1:
        if buchstabe in wort2_liste:
            wort2_liste.remove(buchstabe)
        else:
            return False  # Falls Buchstabe fehlt, ist es kein Anagramm

    return True  # Wenn alle Buchstaben entfernt wurden, ist es ein Anagramm

# Tests
print(anagramm("rat", "tar"))  # True
print(anagramm("listen", "silent"))  # True
print(anagramm("apple", "pale"))  # False
print(anagramm("aabb", "ab"))  # False
print(anagramm("aabb", "baba"))  # True
