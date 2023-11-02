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

    if user_input not in range(1,6):
        print("Invalid input, please choose again.")
        user_interface()

    print(user_input)
    return(user_input)

def parsing_option(user_input):
    
    if user_input == 1:
        exit()

user_interface()