import random

class Dice:
    def __init__(self):
        self.side = 1

    def roll(self):
        self.side = random.randint(1, 6)

    def get_side(self):
        return self.side

class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.dice = Dice()
        self.pet = None

    def roll_dice(self):
        self.dice.roll()

    def get_dice_side(self):
        return self.dice.get_side()

    def set_pet(self, pet):
        self.pet = pet

    def get_pet(self):
        return self.pet

class Mammal:
    def __init__(self, id, species, name, size, weight):
        self.id = id
        self.species = species
        self.name = name
        self.size = size
        self.weight = weight

def main():
    # Create players
    players = [Player(i, f"Player {i}") for i in range(1, 4)]

    # Roll dices
    for player in players:
        player.roll_dice()
        print(f"{player.name} rolled {player.get_dice_side()}")

    # Create mammals
    mammals = [Mammal(i, f"Species {i}", f"Mammal {i}", i*10, i*20) for i in range(1, 13)]

    # Assign pets to players
    for player in players:
        player.set_pet(mammals[player.get_dice_side() - 1])
        print(f"{player.name} got a pet {player.get_pet().name}")

if __name__ == "__main__":
    main()