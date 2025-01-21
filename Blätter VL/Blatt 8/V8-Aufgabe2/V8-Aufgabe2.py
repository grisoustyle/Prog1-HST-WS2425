matrix_1 = [
    [1, 2, 3], #0,0  0,1  0,2
    [4, 5, 6], #1,0  1,1  1,2
    [7, 8, 9]  #2,0  2,1  2,2
]

matrix_2 = [
    [4, 2, 0],
    [4, 0, 4],
    [6, 9, 0]
]

print(len(matrix_1)) #zeilen
print(len(matrix_1[1])) #spalten


def summe_matrix(matrix_1, matrix_2):
    for zeile in range(len(matrix_1)):

        for spalte in range(len(matrix_1[zeile])):

            matrix_1[zeile][spalte] += matrix_2[zeile][spalte]

    return matrix_1

print(summe_matrix(matrix_1,matrix_2))


def produkt_matrix(matrix, wert):
    for zeile in range(len(matrix)):

        for spalte in range(len(matrix[zeile])):
            matrix[zeile][spalte] *= wert

    return matrix

print(produkt_matrix(matrix_2,2))


def matrix_mult_vektor(matrix, vektor):
    ergebnis_matrix = []

    for zeile in range(len(matrix)):
        stellen_ergebnis = 0

        for spalte in range(len(matrix[zeile])):
            stellen_ergebnis += matrix[zeile][spalte] * vektor[spalte]

        ergebnis_matrix.append(stellen_ergebnis)

    return ergebnis_matrix

print(matrix_mult_vektor(matrix_1,[1,3,5]))

def transpose_matrix():
    return