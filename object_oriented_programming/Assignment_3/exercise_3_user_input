class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number: int):
        self.numbers.append(number)
        
    def count_numbers(self):
        return len(self.numbers)
    
    def get_sum(self):
        if self.numbers == 0:
            return 0
        else:
            return sum(self.numbers)
        
    def average(self):
        if self.numbers == 0:
            return 0
        else:
            return sum(self.numbers) / len(self.numbers)
        
    def even_numbers(self):
        even = sum(number for number in self.numbers if number % 2 == 0)
        return even
    
    def odd_numbers(self):
        odd = sum(number for number in self.numbers if number % 2 != 0)
        return odd

def user_integers():
    
    stats = NumberStats()

    while True:
        user_input = int(input("Please type in integer numbers: \n"))
        if user_input == -1:
            break
        stats.add_number(user_input)

    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())
    print("Sum of even numbers: ", stats.even_numbers())
    print("Sum of odd numbers: ", stats.odd_numbers())

def main():
    user_integers()

if __name__ == "__main__":
    main()