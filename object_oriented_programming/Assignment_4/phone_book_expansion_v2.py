class Person:
    def __init__(self, name: str):
        self.name = name
        self.numbers = []
        self.address = None

    def add_number(self, number: str):
        if number == None:
            return self.numbers
        else:
            self.numbers.append(number)
        
    def add_address(self, address: str):
        self.address = address

    def get_numbers(self):
        if not self.numbers:
            return "Number is unknown."
        return self.numbers
    
    def get_address(self):
        if self.address == None:
            return "Address is unknown."
        return self.address

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)

    def add_address(self, name: str, address: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)
    
    def get_entry(self, name: str):
       if name in self.__persons:
           return self.__persons[name].get_numbers(), self.__persons[name].get_address()
       else:
           return None, None

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
    
    def help(self):
        print("Commands: ")
        print("0 to exit")
        print("1 to add entry")
        print("2 to search")
        print("3 to add address")

    def add_entry(self):
        name = input("Enter name: ")
        number = input("Enter number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("Enter name to be searched: ")
        numbers, address = self.__phonebook.get_entry(name)
        if numbers == None and address == None:
            print("Number was not found or is unknown.")
            print("Address was not found or is unknown.")
            return
        if numbers == None and address != None:
            print("Number was not found or is unknown.")
            return
        for number in numbers:
            print(f"{name}: {number}")

    def add_address(self):
        name = input("Enter name: ")
        address = input("Enter address: ")
        self.__phonebook.add_address(name, address)

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("Enter command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()

# code for testing
                
    #part 1
#phonebook = PhoneBook()
#phonebook.add_number("Eric", "02-123456")
#print(phonebook.get_numbers("Eric"))
#print(phonebook.get_numbers("Emily"))
                
    #part 2
#application = PhoneBookApplication()
#application.execute()
                
    #part 3 from itslearning
#person = Person("Eric")
#print(person.name)
#print(person.number)
#print(person.address)
#person.add_number("02-123456")
#person.add_address("Mannerheimintie 10 Helsinki")
#print(person.number)
#print(person.address)
                
    #part 4 from itslearning
#phonebook = PhoneBook()
#phonebook.add_number("Eric", "02-123456")
#print(phonebook.get_entry("Eric"))
#print(phonebook.get_entry("Emily"))

    #part 5 from itslearning
application = PhoneBookApplication()
application.execute()