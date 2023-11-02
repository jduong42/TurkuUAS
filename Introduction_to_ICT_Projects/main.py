# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jduong <juha.duong@edu.turkuamk.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/02 15:52:18 by jduong            #+#    #+#              #
#    Updated: 2023/11/02 15:52:18 by jduong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random_list import *
from search_element import *
from add_element import *

# Made a randomized list with 30 elements as soon as program starts.

random_list = randomize_list()

def user_interface():
    # A Simple user interface for choosing an action.

    print("Please, select the following option:")
    print("Press 1 --> Quit program.")
    print("Press 2 --> To search an element from the list.")
    print("Press 3 --> To add an element to the list.")
    print("Press 4 --> Remove an element from the list.")
    print("Press 5 --> To sort the list.")
    print("Press 6 --> To list all the elements in the list.")

    user_input = int(input("Please choose your option: "))

    if user_input not in range(1,7):
        print("Invalid input, please choose again.")
        user_interface()
    else:
        parsing_option(user_input)

def parsing_option(user_input):
    # Taking the return value of user_interface function and passing into parsing function
    
    if user_input == 1:
        exit()
    #elif user_input == 2:
    #if user_input == 3:
        # New random_list will be returned, when element has been added to the existing list, thus creating a updated list.
        
    #    random_list = add_element(random_list)
    if user_input == 6:
        print(random_list)
      
      
def main():
  # Randomizing a list in the start of the program.

  user_interface()

if __name__ == "__main__":
    main()