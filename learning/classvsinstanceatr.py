class Person:
    species = "Homo sapiens"  # Class attribute
    
    def __init__(self, name, age):
        self.name = name      # Instance attribute
        self.age = age        # Instance attribute

# Access and modify attributes
person1 = Person("Alice", 25)

print(person1.species)   # Output: Homo sapiens
print(person1.name)      # Output: Alice
print(person1.age)       # Output: 25

# Modify instance attributes
person1.age = 26
print(person1.age)       # Output: 26

# Modify class attribute
Person.species = "Human"
print(person1.species)   # Output: Human