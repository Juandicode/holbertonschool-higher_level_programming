#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            # Intentar realizar la división
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            # Si el tipo no es numérico
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            # Si hay una división entre 0
            print("division by 0")
            result = 0
        except IndexError:
            # Si falta un elemento en alguna de las listas
            print("out of range")
            result = 0
        finally:
            # Agregar el resultado (sea válido o 0) a la nueva lista
            new_list.append(result)
    return new_list
