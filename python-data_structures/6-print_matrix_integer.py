#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        formateado_row = []
        for i in row:
            numero_formateado = "{:d}".format(i)
            formateado_row.append(numero_formateado)
        print(" ".join(formateado_row))

# "{:d}".format(i) esto convierte cada 
# numero enter en una cadena con formato decimal ej: 1 -> "1" , 2 -> "2"
