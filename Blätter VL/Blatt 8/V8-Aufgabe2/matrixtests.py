matrix_1 = [
    [1, 2, 3], #0,0  0,1  0,2
    [4, 5, 6], #1,0  1,1  1,2
    [7, 8, 9]  #2,0  2,1  2,2
]
#element[spalte][zeile]

matrix_2 = [
    [4, 2, 0],
    [4, 0, 4],
    [6, 9, 0]
]

vektor = [
    4,
    2,
    7
]



print(len(matrix_1)) #spalten
print(len(matrix_1[1])) #zeilen

multiplikation = 2

index_spalte = -1

neue_zeile = [[],[],[]]

for zeilen in (matrix_1):
    print(f"--\nAktuelle Zeile: {zeilen}")
    index_spalte +=1
    print(f"Spaltenindex: {index_spalte}")
    index_zeile = 0
    for element in zeilen:
        print(f"Aktueller Elementindex: [{index_spalte};{index_zeile}] Element: {element}")
        element *= multiplikation
        print(f"Neues Element {element} an Stelle [{index_spalte};{index_zeile}]")
        (neue_zeile[index_spalte]).append(element)
        index_zeile +=1
        print(f"Neue zeile: {neue_zeile}\n")
