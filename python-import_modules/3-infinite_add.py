#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]  # Excluye el nombre del script
    total = sum(int(arg) for arg in argv)  # Convierte los argumentos a enteros y suma
    print(total)
