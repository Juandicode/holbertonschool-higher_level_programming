#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # si el indice es negatio o mayor al tamaño de la lista
    if idx < 0 or idx >= len(my_list):
        return my_list[:] # devuelve una copia de la lista

    new_list = my_list[:]  # esto cre una copia de la lista orgiinal pa no modificarla
    new_list[idx] = element # reemplaza el elemento en la copia de la lista
    return new_list
