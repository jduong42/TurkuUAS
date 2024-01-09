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

def main():
    lists = print_list()
    order_list(lists)

if __name__ == "__main__":
    main()