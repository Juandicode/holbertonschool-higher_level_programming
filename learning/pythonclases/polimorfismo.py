#!/usr/bin/python3

"""### **Exercise 4: Polymorphism**
Create a class `Shape` with a method `area()` that raises a `NotImplementedError`.
Create two subclasses `Circle` and `Rectangle` that implement the `area()` method.
Write a function that takes a `Shape` object and prints its area. Test it with instances of `Circle` and `Rectangle`.
---"""
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

def print_area(shape):
    print(f"The area is: {shape.area()}")

# Test
circle = Circle(5)
rectangle = Rectangle(4, 6)

print_area(circle)      # Output: The area is: 78.5
print_area(rectangle)   # Output: The area is: 24