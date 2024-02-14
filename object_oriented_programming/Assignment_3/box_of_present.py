class Present:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

class Box:
    def __init__(self):
        self.present = []

    def add_present(self, present: Present):
        self.present.append(present)

    def total_weight(self):
        total = 0
        for present in self.present:
            total += present.weight
        return total

def main():
    #Test the Present class
    """
    book = Present("Ta-Neishi Coates: The Water Dancer", 200)
    print("The name of the present is", book.name, "and it weighs", book.weight, "grams.")
    print("Present:", book)
    """
    #Test the Box class
    
    book = Present("Ta-Neishi Coates: The Water Dancer", 200)
    box = Box()
    box.add_present(book)
    print(box.total_weight())

    cd = Present("Pink Floyd: Dark Side of the Moon", 50)
    box.add_present(cd)
    print(box.total_weight())  

if __name__ == "__main__":
    main()