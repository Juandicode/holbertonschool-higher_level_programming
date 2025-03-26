#!/usr/bin/env python3
class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def suma(self):  # Método de instancia, necesita ser llamado con una instancia
        return self.a + self.b

# Intentar llamar al método sin instanciar la clase dará un error
# Esto dará un TypeError, porque el método 'suma' necesita 'self' como primer parámetro
calc = Calculadora(1, 2)
print(calc.suma())


### este metodo sin static funciona 
