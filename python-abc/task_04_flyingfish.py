class Fish:
    # Clase base que representa un pez
    def swim(self):
        print("The fish is swimming")  # Método para nadar
    
    def habitat(self):
        print("The fish lives in water")  # Método para describir el hábitat del pez

class Bird:
    # Clase base que representa un pájaro
    def fly(self):
        print("The bird is flying")  # Método para volar
    
    def habitat(self):
        print("The bird lives in the sky")  # Método para describir el hábitat del pájaro

class FlyingFish(Fish, Bird):
    # Clase que hereda de Fish y Bird, representando un pez volador
    def fly(self):
        print("The flying fish is soaring!")  # Sobrescribe el método fly para un pez volador
    
    def swim(self):
        print("The flying fish is swimming!")  # Sobrescribe el método swim para un pez volador
    
    def habitat(self):
        print("The flying fish lives both in water and the sky!")  # Sobrescribe el hábitat para reflejar ambos entornos
