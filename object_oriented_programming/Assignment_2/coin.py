# File:         coin.py
# Source:       Tony Gaddis: Starting Out With Python, fourth edition
# Modified by:  Juha Duong
# Description:  Coin object and tossing.

import random

# Class definition

class Coin:
    def __init__(self):
        self.sideup = 'Heads'

    def toss_the_coin(self):

        program_choice = random.randint(0, 3)

        if program_choice == 0:
            self.sideup = 'Heads'
        if program_choice == 1:
            self.sideup = 'Tails'
        if program_choice == 2:
            self.sideup = 'Coin is on its edge.'
        if program_choice == 3:
            self.sideup = 'Coin drops on the ground and dissapears into a rabbit hole.'
        if program_choice == 4:
            self.sideup = 'Coin defies gravity and gets lost on a wormhole in space.'

    def get_sideup(self):

        return self.sideup
    
# Main function definition
    
def main():

    my_coin = Coin()

    print('This side is up:', my_coin.get_sideup())

    print('Tossing the coin ...')
    my_coin.toss_the_coin()

    print('Now this side is up:', my_coin.get_sideup())

# Call the main function
main()