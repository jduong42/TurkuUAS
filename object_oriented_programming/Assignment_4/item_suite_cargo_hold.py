class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight}kg)"

class Suitcase:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.contents = []

    def add_item(self, item):
        if self.current_weight() + item.weight <= self.max_weight:
            self.contents.append(item)
        else:
            print("Adding the item will exceed maximum weight limit.", item)

    def current_weight(self):
        return sum(item.weight for item in self.contents)
    
    def print_items(self):
        for item in self.contents:
            print(item)
    
    def heaviest_item(self):
        if not self.contents:
            return None
        return max(self.contents, key=lambda item: item.weight)

    def __str__(self):
        if len(self.contents) == 1:
            return f"Suitcase (number of item: {len(self.contents)}, max weight: {self.max_weight}kg, current weight: {self.current_weight()}kg)"
        else:
            return f"Suitcase (number of items: {len(self.contents)}, max weight: {self.max_weight}kg, current weight: {self.current_weight()}kg)"
        
class CargoHold():

    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.suitcases = []

    def add_suitcase(self, suitcase):
        if self.current_weight() + suitcase.current_weight() <= self.max_weight:
            self.suitcases.append(suitcase)
        else:
            print("Adding the suitcase will exceed maximum weight limit.", suitcase)

    def current_weight(self):
        return sum(suitcase.current_weight() for suitcase in self.suitcases)
    
    def print_items(self):
        for suitcase in self.suitcases:
            suitcase.print_items()
    
    def __str__(self):
        return f"number of suitcases: {len(self.suitcases)}, space left: {self.max_weight - self.current_weight()}kg"
    
book = Item("ABC Book", 0.200)
phone = Item("Nokai 3210", 0.100)
brick = Item("Brick", 0.400)
