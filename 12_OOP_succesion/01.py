class Animal:
    def Lifeborn(self):
        print('yes')


class Cat:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, race):
        self.race = race


catt = Cat('Tom')
piesel = Dog('kundel')
print(piesel.Lifeborn())
print(piesel.race)
print(catt.name)
