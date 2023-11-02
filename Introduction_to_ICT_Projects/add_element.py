# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    add_element.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jduong <juha.duong@edu.turkuamk.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/02 16:40:53 by jduong            #+#    #+#              #
#    Updated: 2023/11/02 16:40:53 by jduong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from main import random_list

new_list = random_list

def add_element(new_list):
    # Asking the user, what datatype of the element will be

    print(new_list)
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
    print(new_list)

    return(new_list)