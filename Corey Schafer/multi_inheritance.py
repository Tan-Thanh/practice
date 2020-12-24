class First:
    def getClass (self):
        print ("Class first")

class second(First):
    def getClass(self):
        print ("Class second")
class third(First):
    def getClass(self):
        print ("Class third")
class four(second, third):
    def getClass(self):
        super().getClass()
        
class Animal:
    def __init__(self, Animal):
        print (Animal, "là một loài động vật")
class Mammal(Animal):
    def __init__(self, mammal):
        print (mammal, 'là động vật có vú')
        super().__init__(mammal)
class CantFly(Mammal):
    def __init__(self, cantfly):
        print (cantfly, "không biết bay")
        super().__init__(cantfly)
class CantSwim(Mammal):
    def __init__(self, cantswim):
        print (cantswim, "không biết bơi")
        super().__init__(cantswim)
class Fish(CantSwim, CantFly):
    def __init__(sefl, obj):
        super().__init__(obj)
a = Fish("Dolphin")
