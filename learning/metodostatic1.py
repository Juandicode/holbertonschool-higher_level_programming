#!/usr/bin/env python3
class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    @staticmethod
    def suma(a, b):  # Método de instancia, necesita ser llamado con una instancia
        return a + b


print(Calculadora.suma(12, 2))
