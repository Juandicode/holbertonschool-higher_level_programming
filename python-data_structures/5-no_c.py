#!/usr/bin/python3
def no_c(my_string):
    # crea una nueva cadena sin las letras c y C
    new_string = ""  # inicializa una nueva cadena vacía 
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string  # devuelve la nueva cadena sin las letras c y C
