#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]  # Excluye el nombre del script
    argc = len(argv)

    if argc == 0:
        print(f"{argc} arguments.")
    elif argc == 1:
        print(f"{argc} argument:")
        print(f"1: {argv[0]}")
    else:
        print(f"{argc} arguments:")
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")
