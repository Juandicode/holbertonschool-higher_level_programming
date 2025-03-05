class Perro:
    def __init__(self, edad, peso, nombre):
        self.edad = edad
        self.peso = peso
        self.nombre = nombre

    def mostrar_nombre(self,altura):
        altura = 15
        print(f"mi nombre es {self.nombre}, y tengo {self.edad} años y peso {self.peso} kg, y tengo una altura de {altura} cm")
        
    def verificar_edad(self, edad):
        if edad <= 5: 
            return("soy menor")
        else:
            return("soy mayor")

perro1= Perro(5, 10, "dino")
perro1.mostrar_nombre(10)
print(perro1.verificar_edad(1))