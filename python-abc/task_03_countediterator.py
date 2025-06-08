class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)  # Crea un iterador a partir del iterable dado
        self.count = 0  # Inicializa el contador de elementos iterados

    def __next__(self):
        item = next(self.iterator)  # Obtiene el siguiente elemento del iterador
        self.count += 1  # Incrementa el contador
        return item  # Devuelve el elemento obtenido

    def get_count(self):
        return self.count  # Devuelve el número de elementos iterados
