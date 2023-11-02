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

# Made a randomized list with 30 elements as soon as program starts.

random_list = randomize_list()

# A Simple user interface for choosing an action.

def user_interface():

    print("Please, select the following option:")
    print("Press 1 --> Quit program.")
    print("Press 2 --> To search an element from the list.")
    print("Press 3 --> To add an element to the list.")
    print("Press 4 --> Remove an element from the list.")
    print("Press 5 --> To sort the list.")
    print("Press 6 --> To list all the elements in the list.")

    user_input = int(input("Please choose your option: "))

    # Checking that the input is in range and valid
    
    if user_input not in range(1,7):
        print("Invalid input, please choose again.")
        user_interface()
    else:
        parsing_option(user_input)

# Taking the return value of user_interface function and passing into parsing function
def parsing_option(user_input):
    
      if user_input == 1:
        print('\n')
        exit()
      if user_input == 2:
        # Function compares given value with the current list.

        compare_elements(random_list)
        user_interface()
      if user_input == 3:
        # New random_list will be returned, when element has been added to the existing list, thus creating a updated list.
          
        add_element(random_list)
        print('\n')
        user_interface()
      if user_input == 4:
        # Function removes an element based on index.

        remove_element(random_list)
        print('\n')
        user_interface()
      if user_input == 5:
        # Function sorts the elements 1st strings, 2nd integers and 3rd floats.

        custom_sort(random_list)
        print('\n')
        user_interface()
      if user_input == 6:
        # Function prints the current list, but for some reason it does not work after sorting the list
         
        print(random_list)
        print('\n')
        user_interface()

# Asking the user, what element to delete based on the index

def remove_element(list):


    print("Here is the existing list in from of: index - value")
    for (i, item) in enumerate(list):
       print("index:", i, "value", item)

    user_input = int(input("What index you want to remove from the list? Give a valid index number: \n"))
    list.pop(user_input)

    return(list)

# Asking the user, what datatype of the element will be and then ask what value the user wants to give it

def add_element(new_list):

    data_type = input("What datatype you want the new element to be? Choose from: integer, float or string\n")
    
    # Checking if the input requirements are met for new element:

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

# Function asks first what datatype user wants to search and after that ask what value in the specific datatype. Also, checks if datatype is correct or not.

def compare_elements(compare_list):
  
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

# A sorting function that extract a value from each element in the list, which is used for comparison during the sorting process. Strings are given the highest priority, followed by integers and then floats, with other data types considered last. 

def custom_sort(random_list):
  def custom_key(value):
      if isinstance(value, str):
         return(0, value)
      elif isinstance(value, int):
         return(1, value)
      elif isinstance(value, float):
         return(2, value)
      else:
         return(3, value)

  new_list = sorted(random_list, key=custom_key)

  return (new_list)
         
    
def main():
  user_interface()

if __name__ == "__main__":
    main()