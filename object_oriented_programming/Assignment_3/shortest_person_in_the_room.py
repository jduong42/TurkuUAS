class Person:
    def __init__(self, name: str, height: float):
        self.name = name
        self.height = height
    
    def __str__(self):
        return f"{self.name} ({self.height} cm)"

class Room:
    def __init__(self):
        self.persons = []
    
    def add(self, person: Person):
        self.persons.append(person)
   
    def is_empty(self):
        if len(self.persons) == 0:
            return True
        else:
            return False
        
    def print_contents(self):
        if len(self.persons) == 0:
            return "The room is empty"
        else:
            for person in self.persons:
                print(person)

    def combined_height(self):
        return sum([person.height for person in self.persons])
    
    def shortest(self):
        if len(self.persons) == 0:
            return None
        else:
            return min(self.persons, key=lambda person: person.height)
        
    def remove_shortest(self):
        if self.is_empty():
            return None
        else:
            shortest_person = self.shortest()
            self.persons.remove(shortest_person)
            return shortest_person
    
room = Room()

#Test 1
"""
print("Is the room empty?", room.is_empty())
room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Ally", 166))
room.add(Person("Nina", 162))
room.add(Person("Dorothy", 175))
print("Is the room empty?", room.is_empty())
room.print_contents()
"""
#Test 2
room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Ally", 166))
room.add(Person("Nina", 162))
room.add(Person("Dorothy", 175))
print("Is the room empty?", room.is_empty())
print("Shortest:", room.shortest())
room.print_contents()

#Test 3
removed = room.remove_shortest()
print(f"Removed from room: {removed.name}")
print()
room.print_contents()
