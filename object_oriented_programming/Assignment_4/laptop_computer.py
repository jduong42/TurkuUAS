class Computer:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

class LaptopComputer(Computer):
    def __init__(self, name, speed, weight):
        super().__init__(name, speed)
        self.weight = weight

    def __str__(self):
        return f"{self.name}, {self.speed} MHz, {self.weight} kg"
 