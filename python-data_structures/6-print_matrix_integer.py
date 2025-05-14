#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        formateado_row = []  # lista vacía para almacenar los números formateados
        for i in row:  # itera sobre cada elemento de la fila
            numero_formateado = "{:d}".format(i)  # formatea el número como cadena
            formateado_row.append(numero_formateado)  # agrega el número formateado a la lista
        # une los números formateados con un espacio y los imprime
        # el join une los elementos de la lista con un espacio entre ellos
        print(" ".join(formateado_row))

# "{:d}".format(i) esto convierte cada
# numero enter en una cadena con formato decimal ej: 1 -> "1" , 2 -> "2"
