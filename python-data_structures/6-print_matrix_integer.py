#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row:
            formatted_number = "{:d}".format(i)
            formatted_row.append(formatted_number)
        print(" ".join(formatted_row))


# "{:d}".format(i) esto convierte cada numero enter en una cadena con formato decimal ej: 1 -> "1" , 2 -> "2"