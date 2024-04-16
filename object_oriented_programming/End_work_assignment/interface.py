from user_class import User
from helper_functions import ft_regular, ft_smart, phone_to_user, remove_phone_from_user

# Global variables
user_list = []
phone_list = []

def interface():
    print("Welcome to the phone trade program!")

    while True:
        print("Choose following options:")
        print("1. Add user.")
        print("2. Add phone.")
        print("3. See users.")
        print("4. See phones.")
        print("5. Set phone for user.")
        print("6. Remove phone from user.")
        print("0. Exit.")
        user_input = int(input("Choose option: \n"))

        if user_input == 1:
            first_name = input("Enter user's first name: ")
            last_name = input("Enter user's last name: ")
            age = int(input("Enter user's age: "))
            phone = None
            user = User(first_name, last_name, age, phone)
            user_list.append(user)

        elif user_input == 2:
            print("Is the phone a smartphone or a regular phone?")
            print("1. Regular phone.")
            print("2. Smartphone.")
            phone_input = int(input("Choose option: "))

            if phone_input == 1:
                phone = ft_regular()
                phone_list.append(phone)
            elif phone_input == 2:
                phone = ft_smart()
                phone_list.append(phone)

        elif user_input == 3:
            if len(user_list) == 0:
                print("No users.")
            for user in user_list:
                print(user)

        elif user_input == 4:
            if len(phone_list) == 0:
                print("No phones.")
            for phone in phone_list:
                print(phone)
        
        elif user_input == 5:
            phone = phone_to_user(user_list, phone_list)
            if phone != None:
                user, phone = phone
                phone_list.remove(phone)
        
        elif user_input == 6:
            phone = remove_phone_from_user(user_list)
            if phone != None:
                phone_list.append(phone)

        elif user_input == 0:
            print("Exiting the program.")
            exit()
    