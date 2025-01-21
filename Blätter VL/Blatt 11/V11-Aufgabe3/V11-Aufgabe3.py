'''try:
    numerator = int(input("Bitte geben Sie den Zähler ein: "))
    try:
        denominator = int(input("Bitte geben Sie den Nenner ein: "))
        result = numerator / denominator 
        print(f"Ergebnis: {result}")
    except ValueError:
        print("Bei Nenner nur Int erlaubt!")
except ValueError:
    print("Bei Zähler nur Int erlaubt!")
finally:
    print("Programm beendet.")'''


try:
    numerator = int(input("Bitte geben Sie den Zähler ein: "))
    denominator = int(input("Bitte geben Sie den Nenner ein: "))
    result = numerator / denominator
except ValueError:
    print("Fehler: Nur ganze Zahlen sind erlaubt!")
except ZeroDivisionError:
    print("Fehler: Division durch Null ist nicht erlaubt!")
else:
    print(f"Ergebnis: {result}")
finally:
    print("Programm beendet.")
