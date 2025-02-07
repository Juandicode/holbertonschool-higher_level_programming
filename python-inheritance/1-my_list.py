#!/usr/bin/python3

class MyList(list):
    """Clase que hereda de list y proporciona un método para imprimir la lista ordenada."""
    
    
	def print_sorted(self):
        """Imprime la lista en orden ascendente."""
        print(sorted(self))
