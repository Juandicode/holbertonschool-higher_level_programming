#!/usr/bin/python3
"""
anda leyendo la letra masomenos Ejercicio
Clases:

Clase Persona: Contiene atributos nombre y edad, y un método obtener_informacion.
Clase Usuario: Hereda de Persona y añade un atributo numero_de_usuario. Sobrescribe el método obtener_informacion para incluir el número de usuario.
Clase Autor: Contiene atributos nombre y nacionalidad, y un método obtener_informacion que devuelve información sobre el autor.
Clase Libro: Contiene atributos titulo, anio_publicacion, y un objeto de la clase Autor. Incluye un método obtener_informacion que devuelve información sobre el libro y su autor.
Clase Biblioteca: Contiene una lista de libros y una lista de usuarios. Incluye métodos para agregar libros y usuarios, y un método para mostrar todos los libros disponibles.
Requisitos:

Implementa las clases según la descripción anterior.
Crea al menos dos autores, tres libros (cada uno con un autor diferente), y dos usuarios.
Agrega los libros a la biblioteca y los usuarios a la biblioteca.
Imprime la información de todos los libros en la biblioteca y la información de los usuarios.
"""

class Persona:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    def obtener_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, mi peso es {self.peso}"

#eso es herncia, hereda 2 arributos y tiene uno propio de esta clase

class Usuario(Persona):
    def __init__(self, nombre, edad, peso, numero_de_usuario):
        super().__init__(nombre, edad, peso)
        self.numero_de_usuario = numero_de_usuario
    def obtener_informacion(self):
        return (f"Nombre: {self.nombre} Edad: {self.edad}, mi nro de usuario es : {self.numero_de_usuario} y peso {self.peso}  ")

class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def obtener_informacion(self):
        return f"{self.nombre} es el autor del libro su nacionalidad es {self.nacionalidad}"
#esto es composicion de la clase libro con autor     

class Libro:
    def __init__(self, titulo, año_publicacion, autor):
        self.titulo = titulo
        self.año_publicacion = año_publicacion
        self.autor = autor

    def obtener_informacion(self):
        return f"titulo del libro: {self.titulo}, año publicado {self.año_publicacion} {self.autor.obtener_informacion()}"

class Biblioteca:
    def __init__(self, usuarios=[], libros=[]):
        self.usuarios = usuarios
        self.libros = libros
    
    def agregar_usuarios(self, usuario):
        self.usuarios.append(usuario)
    #   return f"usuario {self.usuario.nombre}ha sigo agregado con exito"
        return f"usuario {usuario.nombre} ha sigo agregado con exito"        

    def agregar_libros(self, libro):
        self.libros.append(libro)
        return f"nombre del libro {libro.obtener_informacion()}"

    def listar_libros(self):
        for libro in self.libros:
            print(libro.titulo)


#crear instancias , cuando son letras van con comillas y si son numeros no 



#autor1 = Autor("jhon lenon", "usa")
#autor = Autor("kiyosaki", "japon")
#libro = Libro("padre rico padre pobre", 2007, autor)
#libro2 = Libro("como hacerse riko", 2008, autor1)
#usuario1 = Usuario("juan", 22, 44200)
#usuario2 = Usuario("pedro", 23, 44450)
#biblioteca = Biblioteca([usuario1, usuario2],[libro, libro2])

#persona45 = Persona ("juandi", 23, 70)
usuario = Usuario ("juan", 23, 5500, 70)


#print(persona45.obtener_informacion())
print(usuario.obtener_informacion())
#print(biblioteca.listar_libros())
#print(biblioteca.agregar_usuarios(usuario1))
#print(biblioteca.agregar_libros(libro2))
