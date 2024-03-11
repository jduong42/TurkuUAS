class Mammal:
    def __init__(self, name: str, age: int, sex: str):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def move(self):
        print(f"{self.name} is moving")

class Cat(Mammal):
    def __init__(self, name: str, age: int, sex: str, breed: str, colour: str):
        super().__init__(name, age, sex)
        self.breed = breed
        self.colour = colour

        def chaseMice(self):
            print(f"{self.name} is chasing mice")
        
        def groom(self):
            print(f"{self.name} is grooming")

class Dog(Mammal):
    def __init__(self, name: str, age: int, sex: str, breed: str, colour: str):
        super().__init__(name, age, sex)
        self.breed = breed
        self.colour = colour

        def buryFood(self):
            print(f"{self.name} is burying food")

        def bark(self):
            print(f"{self.name} is barking")


class Mouse(Mammal):
    def __init__(self, name: str, age: int, sex: str, colour: str, isNocturnal: bool, burrowingAbility: bool):
        super().__init__(name, age, sex)
        self.colour = colour
        self.isNocturnal = isNocturnal
        self.burrowingAbility = burrowingAbility

        def squeak(self):
            print(f"{self.name} is squeaking")

        def gnaw(self):
            print(f"{self.name} is gnawing")

