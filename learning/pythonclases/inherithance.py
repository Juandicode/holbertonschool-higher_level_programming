#!/usr/bin/python3
"""
Exercise 2: Inheritance**
Create a base class `Animal` with:
Attributes: `name`, `species`
Method: `make_sound()` (prints "Some generic sound")
Create a subclass `Dog` that overrides `make_sound()` to print "Woof!"
Instantiate objects of both classes and call `make_sound()` for each.
"""

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")


animal = Animal("aguila", "ave")
animal.make_sound()

dog = Dog("Firulais", "can")
dog.make_sound()