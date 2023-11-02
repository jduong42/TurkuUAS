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

    data_type = input("What datatype you want the new element to be? Choose from: integer, float or string\n")
    
    #Checking if the input requirements are met for new element:

    if data_type not in ["Integer", "integer", "int", "Float", "float", "String", "string", "str"]:
        print("Invalid input, choose again.")
        add_element(new_list)
    elif data_type == "Float" or "float":
        new_element = float(input("Inputa valid float value: "))
    elif data_type == "Integer" or "integer" or "int":
        new_element = int(input("Input a valid integer value: "))
    elif data_type == "String" or "string" or "str":
        new_element = str(input("Input a valid string: "))
    
    new_list.append(new_element)

    return(new_list)