class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def get_details(self):
        return f"Name: {self.name}, Salary: ${self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    
    def get_details(self):
        return f"{super().get_details()}, Team Size: {self.team_size}"

# Test
emp = Employee("Bob", 50000)
mgr = Manager("Alice", 80000, 5)

print(emp.get_details())  # Output: Name: Bob, Salary: $50000
print(mgr.get_details()) # Output: Name: Alice, Salary: $80000, Team Size: 5