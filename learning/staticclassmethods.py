class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def create_default(cls):
        return cls()  # Returns a default instance

# Test static method
print(Calculator.add(3, 5))  # Output: 8

# Test class method
calc = Calculator.create_default()
print(calc.add(2, 4))       # Output: 6