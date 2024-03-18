import random

class Mammal:
    def __init__(self, name: str, age: int, sex: str):
        self.name = name
        self.age = age
        self.sex = sex

    def toEatPrey(self):
        print(f"{self.name} is trying to eat the prey.")
        if self.prey.checkIfEscape() == True:
            print(f"{self.name} has eaten the prey: {self.prey.name}.")
        else:
            print(f"{self.prey.name} managed to escape.")

    def toSleep(self):
        print(f"{self.name} is going to sleep.")

    def toHuntPrey(self):
        print(f"{self.name} is hunting for prey.")

    def moveToHabitat(self):
        print(f"{self.name} is moving to the habitat.")
        if self.habitat.checkIfSpace() == True:
            self.habitat.current_capacity += 1
            self.habitat.predator = True
            print(f"{self.name} has moved to the habitat.")
        else:
            print(f"{self.name} could not move to the habitat.")

class Habitat:
    def __init__(self, name: str, location: str, current_capacity: int, predator: bool):
        self.name = name
        self.location = location
        self.current_capacity = current_capacity
        self.max_capacity = 20
        self.predator = False

    def checkIfSpace(self):
        if self.current_capacity < self.max_capacity:
            return True
        else:
            return False
        
    def checkIfSpaceAndMammal(self):
        if self.current_capacity < self.max_capacity & self.predator == False:
            return True
        else:
            return False


class Prey:
    def __init__(self, name: str, animal_type: str):
        self.name = name
        self.animal_type = animal_type

    def checkIfEscape():
        escape = random.randint(0, 6)
        if escape >= 3:
            return True
        else:
            return False
        
    def toSleep():
        print(f"{self.name} is going to sleep.")

    def toTauntMammal(self):
        print(f"{self.name} is taunting the mammal.")
        
    def moveToHabitat(self):
        print(f"{self.name} is moving to the habitat.")
        if self.habitat.checkIfSpace() == True & self.habitat.predator == False:
            self.habitat.current_capacity += 1
            print(f"{self.name} has moved to the habitat.")
        else:
            print(f"{self.name} could not move to the habitat, because there are one or more predators in the habitat.")

