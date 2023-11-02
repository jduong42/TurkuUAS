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
#from search_element import *
#from add_element import *

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
        print('\n')
        exit()
      if user_input == 2:
          # kommentti

          compare_elements(random_list)
          user_interface()
      if user_input == 3:
          # New random_list will be returned, when element has been added to the existing list, thus creating a updated list.
          
          add_element(random_list)
          print('\n')
          user_interface()
      if user_input == 4:
          # kommentti

          remove_element(random_list)
          print('\n')
          user_interface()
      if user_input == 6:
        print(random_list)
        print('\n')
        user_interface()

def remove_element(list):
   # Asking the user, what element to delete based on the index

    print("Here is the existing list in from of: index - value")
    for (i, item) in enumerate(list):
       print("index:", i, "value", item)

    user_input = int(input("What index you want to remove from the list? Give a valid index number: \n"))
    list.pop(user_input)

    return(list)


def add_element(new_list):
    # Asking the user, what datatype of the element will be

    data_type = input("What datatype you want the new element to be? Choose from: integer, float or string\n")
    
    #Checking if the input requirements are met for new element:

    if data_type not in ["Integer", "integer", "int", "Float", "float", "String", "string", "str"]:
        print("Invalid input, choose again.")
        add_element(new_list)
    if data_type in ["Float", "float"]:
        new_element = float(input("Input a valid float value: "))
    if data_type in ["Integer", "integer", "int"]:
        new_element = int(input("Input a valid integer value: "))
    if data_type in ["String", "string", "str"]:
        new_element = str(input("Input a valid string: "))
    
    new_list.append(new_element)

    return(new_list)

def compare_elements(compare_list):
    # Function asks first what datatype user wants to search and after that ask what value in the specific datatype. Also, checks if datatype is correct or not.
  
    data_type = input("Type what datatype you would like to find from the list? Choose from: integer, float or string:\n")

    if data_type not in ["Integer", "integer", "int", "Float", "float", "String", "string", "str"]:
        print("Invalid input, choose again.")
        compare_elements(compare_list)
    if data_type in ["Float", "float"]:
      user_input = float(input("What float value you would like to find in the list?\n"))
      for x in compare_list:
        if x == user_input:
            print("The value was found in the list\n")
    if data_type in ["Integer", "integer", "int"]:
      user_input = int(input("What integer value you would like to find in the list?\n"))
      for x in compare_list:
        if x == user_input:
            print("The value was found in the list\n")
    if data_type in ["String", "string", "str"]:
      user_input = input("What string value you would like to find in the list?\n")
      for x in compare_list:
        if x == user_input:
            print("The value was found in the list\n")
    else:
       print("The value was not found in the list\n")
    
      
def main():
  user_interface()

if __name__ == "__main__":
    main()