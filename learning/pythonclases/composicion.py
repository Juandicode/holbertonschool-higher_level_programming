#!/usr/bin/python3
"""
Ejercicio de Composición
Descripción: Crea un sistema para modelar un Estudiante y un Curso.

Clase Curso:

Atributos:
nombre: el nombre del curso (por ejemplo, "Matemáticas").
codigo: un código único para el curso (por ejemplo, "MAT101").

Métodos:
__init__: inicializa los atributos.
obtener_informacion: devuelve una cadena con la información del curso.
Clase Estudiante:

Atributos:
nombre: el nombre del estudiante.
edad: la edad del estudiante.
curso: una instancia de la clase Curso que representa el curso en el que está inscrito el estudiante.
Métodos:
__init__: inicializa los atributos.
obtener_informacion: devuelve una cadena con la información del estudiante y el curso en el que está inscrito.
Instrucciones
Define las clases Curso y Estudiante según la descripción anterior.
Crea una instancia de Curso y una instancia de Estudiante que esté inscrito en ese curso.
Imprime la información del estudiante y del curso utilizando el método obtener_informacion."""
class Curso:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
    
    def obtener_informacion(self):
        return f"Curso: {self.nombre} (Código: {self.codigo})"


class Estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
    
    def obtener_informacion(self):
        return f" Estudiante: {self.nombre},Edad: {self.edad}\n{self.curso.obtener_informacion()}"


# Creación de instancias
curso_matematicas = Curso("Matemáticas", "MAT101")
estudiante_juan = Estudiante("Juan Pérez", 20, curso_matematicas)

# Mostrar información
print(estudiante_juan.obtener_informacion())