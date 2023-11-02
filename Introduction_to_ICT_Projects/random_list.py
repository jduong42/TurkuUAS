# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    random_list.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jduong <juha.duong@edu.turkuamk.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/02 16:11:30 by jduong            #+#    #+#              #
#    Updated: 2023/11/02 16:11:30 by jduong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def randomize_list():

    # Create an empty list to store the random elements

    random_list = []

     # Define the data types you want to include

    data_types = [int, float, str]

    # Generate 30 random elements

    for i in range(30):
      # Choose a random data type

        data_type = random.choice(data_types)

        # Generate a random value of the chosen data type

        if data_type == int:
          random_element = random.randint(1, 100)
        elif data_type == float:
          random_element = random.uniform(1.0, 100.0)
        else:
          
          # For strings, you can generate random strings of varying lengths

          random_element = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz'))

        # Append the random element to the list

        random_list.append(random_element)
    
    return(random_list)

