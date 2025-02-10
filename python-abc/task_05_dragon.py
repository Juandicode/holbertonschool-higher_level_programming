class SwimMixin:
    # Mixin que proporciona la habilidad de nadar
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    # Mixin que proporciona la habilidad de volar
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    # La clase Dragon hereda de SwimMixin y FlyMixin, obteniendo ambas habilidades
    def roar(self):
        print("The dragon roars!")
