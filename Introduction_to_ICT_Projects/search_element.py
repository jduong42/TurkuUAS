# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    search_element.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jduong <juha.duong@edu.turkuamk.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/02 16:22:01 by jduong            #+#    #+#              #
#    Updated: 2023/11/02 16:22:01 by jduong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from main import random_list

compare_list = random_list
print(compare_list)

def compare_elements(compare_list):
    # lisää kommentti

    user_input = input("Type what you like to find from the list:\n")
    indices = [i for i, x in enumerate(compare_list) if x == user_input]
    print(indices)

    return (indices)