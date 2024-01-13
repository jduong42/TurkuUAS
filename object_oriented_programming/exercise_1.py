import random

def print_hello():
    print("Hello")

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

    while True:
        user_input = input("Write an integer number. If you want to quit adding numbers, write quit.\n")
        new_list.append(user_input)
        if user_input == "quit":
            new_list.remove("quit")
            break
    
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
    
    
    print("Number of negative integers is:", len(negative_list))
    print("Sum of positive integers divisible by three is:", sum(pos_list_div_3))
    print("Number of even integers is:", count)

def arithmetic_progression():

    ap_max = int(input("Give a valid integer value to describe the limit of Arithmetic Progression.\n"))
    
    if ap_max < 0:
        print("The number of terms that appear in the Arithmetic Progression is", 0, "\n")
        print("The sum of the terms is", 0, "\n")
        print("The sum of the squared terms is", 0, "\n")
    else:
        number_of_terms = int(((ap_max - 3) / 3 + 1))
        sum_of_terms = number_of_terms / 2 * (2 * 3 + (number_of_terms - 1) * 3)
        sum_of_squared_terms = number_of_terms / 6 * (2 * 3 + (number_of_terms - 1) * 3) * (3 + (109 - 1) * 3 + 3)
       
        print("The number of terms that appear in the Arithmetic Progression is", number_of_terms, "\n")
        print("The sum of the terms is", sum_of_terms, "\n")
        print("The sum of the squared terms is", sum_of_squared_terms, "\n")

def rps():

    print("****** Welcome to Rock-Paper-Scissors game ******\n" + "The first who wins 3 rounds wins the whole game!\n")

    p_win = 0
    c_win = 0

    while p_win < 3 and c_win < 3:

        user_input = str(input("Choose one of following: Rock, Paper, Scissors.\n"))
        computer_input = random.randint(0,100)

        if computer_input < 33 and computer_input >= 0:
            computer_chose = "rock"
        if computer_input < 66 and computer_input >= 33:
            computer_chose = "paper"
        if (computer_input) < 100 and computer_input >= 66:
            computer_chose = "scissors"
        
        if user_input.lower() == computer_chose:
            print("It's a tie! Play again!\n")
        if user_input.lower() == "rock" and computer_chose == "paper":
            c_win += 1
            print("Computer wins! You lost! :( \n")
        if user_input.lower() == "rock" and computer_chose == "scissors":
            p_win += 1
            print("You win! Computer lost! :) \n")
        if user_input.lower() == "paper" and computer_chose == "scissors":
            c_win += 1
            print("Computer wins! You lost! :( \n")
        if user_input.lower() == "paper" and computer_chose == "rock":
            p_win += 1
            print("You win! Computer lost! :)\n")
        if user_input.lower() == "scissors" and computer_chose == "rock":
            c_win += 1
            print("Computer wins! You lost! :( \n")
        if user_input.lower() == "scissors" and computer_chose == "paper":
            p_win += 1
            print("You win! Computer lost! :)\n")
        print("You have", p_win, "points and computer has", c_win, "points.\n")
    
    if p_win == 3:
        print("Congratulations! You won the game!\n")
    else:
        print("Unfortunately computer won! Try again! \n")

def return_a_number():

    number = random.randint(1, 6)
    
    return (number)

def main():
    #print_hello()
    #lists = print_list()
    #order_list(lists)
    #read_integers()
    #arithmetic_progression()
    #rps()
    print("Random number is:", return_a_number())


if __name__ == "__main__":
    main()