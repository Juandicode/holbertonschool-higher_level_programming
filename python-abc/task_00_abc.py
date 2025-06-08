from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

if __name__ == "__main__":
    bobby = Dog()
    garfield = Cat()
    
    print(bobby.sound())  # Output: Bark
    print(garfield.sound())  # Output: Meow
    
    # Descomentar la siguiente línea causará un error, ya que Animal es abstracto
    # animal = Animal()
