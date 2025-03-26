class Flyable:
    def fly(self):
        print("I can fly!")

class Swimmable:
    def swim(self):
        print("I can swim!")

class Duck(Flyable, Swimmable):
    pass

# Test
duck = Duck()
duck.fly()   # Output: I can fly!
duck.swim()  # Output: I can swim!