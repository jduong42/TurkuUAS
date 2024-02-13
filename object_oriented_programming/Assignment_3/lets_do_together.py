#MOOC.fi decreasing counter:

class DecreasingCounter:

    def __init__(self, initial_value: int):
        self.value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        
        if self.value == 0:
            return self.value
        self.value = self.value - 1

    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = initial_value

if __name__ == "__main__":
    counter = DecreasingCounter(10)
    #prints at the beginning stage:
    counter.print_value()
    # Part 1 The program should always decrese the amount in the self.value stored in the counter by 1
    # 10 -> 9 -> 8 ...

    """ counter.decrease()
    counter.print_value()
    counter.decrease()
    counter.print_value() """
    # Part 2
    """ counter = DecreasingCounter(2)
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter.decrease() """
    # Part 3
    """ counter = DecreasingCounter(100)
    counter.print_value()
    counter.set_to_zero()
    counter.print_value() """
    #Part 4
    """ counter = DecreasingCounter(55)
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.print_value()
    counter.reset_original_value()
    counter.print_value() """