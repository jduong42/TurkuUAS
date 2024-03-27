class Mammal:
    def __init__(self):
        self.state = "Idling"

    def toHunt(self):
        if self.state == "Idling":
            self.state = "Hunting"

    def toEat(self):
        if self.state == "Hunting":
            self.state = "Eating"
        if self.state == "Idling":
            self.state = "Eating"
        if self.state == "Resting":
            self.state = "Eating"

    def toRest(self):
        if self.state == "Eating":
            self.state = "Resting"
        if self.state == "Idling":
            self.state = "Resting"

