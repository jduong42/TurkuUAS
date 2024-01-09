import random

def print_list():

    number_list = []
    str_list = []

    for i in range(10):
        number = input("Write a number.\n")
        
        try:
            int(number)
            number_list.append(number)
        except:
            float(number)
            number_list.append(number)

    for i in range(10):
        user_string = input("Write a string/word/sentence/etc.\n")
        str_list.append(user_string)

    print(number_list)
    print(str_list)

    number_list = []

    for i in range(10):
        number_list.append(random.randrange(-abs(32767), 32767))
    
    print(number_list)
    return(number_list, str_list)

def order_list(lists):

    first_list, second_list = lists

    first_list.sort()
    second_list.sort()

    print(first_list)
    print(second_list)

    return 

def read_integers():
    
    new_list = []
    user_input = 1

    while user_input != '0':
        user_input = input("Write an integer number. If you want to quit adding numbers, press 0.\n")
        new_list.append(user_input)
    
    negative_list = []
    pos_list_div_3 = []
    i = 0
    count = 0

    while i < len(new_list):
        if int(new_list[i]) < 0:
            negative_list.append(int(new_list[i]))
        if int(new_list[i]) % 3 == 0 and int(new_list[i]) > 0:
            pos_list_div_3.append(int(new_list[i]))
        if int(new_list[i]) % 2 == 0 and int(new_list[i]) != 0:
            count += 1
        i += 1
    
    
    print(negative_list)
    print(sum(pos_list_div_3))
    print(count)


def main():
    #lists = print_list()
    #order_list(lists)
    read_integers()

if __name__ == "__main__":
    main()