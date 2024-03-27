from random import getrandbits

class Mammal:
    def __init__(self, name):
        self.name = name
        self.hunger_status = None
        self.tiredness_status_status = None

    def toEat(self):
        self.hunger_status = bool(getrandbits(1))

        if self.hunger_status == True:
            scan_prey = input("Do you want to search for prey? (y/n): ")
            if scan_prey == "y":
                print("You found a prey!")
                prey_escape = bool(getrandbits(1))
                if prey_escape == True:
                    print("The prey escaped! And you have to content yourself with food from the environment.")
                    exit()
                else:
                    print("You caught the prey and now you can eat.")
                    exit()
            else:
                print("You didn't find a prey so you are content to find food from the environment.")
                exit()

    def toRest(self):
        self.tiredness_status = bool(getrandbits(1))
        print(self.tiredness_status)

        if self.tiredness_status == True:
            print("You are tired and need to rest.")
            prey_encounter = bool(getrandbits(1))
            if prey_encounter == True:
                print("You encountered a predator while resting.")
                escape_chance = bool(getrandbits(1))
                if escape_chance == True:
                    print("You managed to escape from the predator and now you can rest.")
                    exit()
                else:
                    print("You were perished.")
                    exit()
            else:
                print("You rested safely.")
                exit()
        else:
            print("You are not tired.")
            exit()
