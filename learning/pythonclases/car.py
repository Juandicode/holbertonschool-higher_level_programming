#!/usr/bin/python3
"""### **Exercise 1: Basic Class and Object**
Create a class `Car` with the following attributes:
`brand`
`model`
`year`
Add a method `display_info()` to print the details of the car.
Instantiate an object of the `Car` class and call the `display_info()` method.
---"""
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        return (f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")
    
car = Car("Ford", "Fiesta", 2010)

print(car.display_info())