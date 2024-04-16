from phone_class import Phone, SmartPhone

def ft_regular():
    brand = input("Enter phone's brand: ")
    model = input("Enter phone's model: ")
    year_of_publish = int(input("Enter phone's year of publish: "))
    phone = Phone(brand, model, year_of_publish)
    return phone

def ft_smart():
    brand = input("Enter phone's brand: ")
    model = input("Enter phone's model: ")
    year_of_publish = int(input("Enter phone's year of publish: "))
    os = input("Enter phone's operating system: ")
    sd_card_slot = bool(input("Does the phone have an SD card slot? "))
    sim_card = bool(input("Does the phone have a SIM card slot? "))
    phone = SmartPhone(brand, model, year_of_publish, os, sd_card_slot, sim_card)
    return phone

def phone_to_user(user_list, phone_list):
    # Check if there are any users or phones
    if len(user_list) == 0:
        print("No users to assign phone to.")
        return None
    if len(phone_list) == 0:
        print("No phones to assign user to.")
        return None
    print("Choose user:")

    # Ask the user to choose a user
    for index, user in enumerate(user_list):
        print(f"{index + 1}. {user.first_name} {user.last_name}")
    user_input = int(input("Choose user: ")) - 1
    print("Choose phone:")

    # Ask the user to choose a phone
    for index, phone in enumerate(phone_list):
        print(f"{index + 1}. {phone.brand} {phone.model}")
    phone_input = int(input("Choose phone: ")) - 1
    user = user_list[user_input]
    phone = phone_list[phone_input]
    user.set_phone(phone)
    print(f"{phone.brand} {phone.model} was set for {user.first_name} {user.last_name}.")
    return user, phone

def remove_phone_from_user(user_list):
    # Check if there are any users
    if len(user_list) == 0:
        print("No users to remove phone from.")
        return None
    
    # Ask the user to choose a user
    for index, user in enumerate(user_list):
        print(f"{index + 1}. {user.first_name} {user.last_name}")
    user_input = int(input("Choose user: ")) - 1
    user = user_list[user_input]

    # Check if the user has any phones
    if not user.get_phone():
        print(f"{user.first_name} {user.last_name} does not have any phones.")
        return None

    # Ask the user to choose a phone
    phone_list = user.get_phone()
    for index, phone in enumerate(phone_list):
        print(f"{index + 1}. {phone.brand} {phone.model}")
    phone_input = int(input("Choose phone: ")) - 1
    phone_to_remove = phone_list[phone_input]

    # Remove the phone from the user
    user.remove_phone(phone_to_remove)
    print(f"{phone_to_remove.brand} {phone_to_remove.model} was removed from {user.first_name} {user.last_name}.")
    return phone_to_remove

def print_phone_details(phone): # This function is polymorphic, it can be used for both Phone and SmartPhone objects
    print(phone)  # This will call the __str__ method of the Phone or SmartPhone object

    # Check if the phone is a SmartPhone 
    if isinstance(phone, SmartPhone):
        print(f"OS: {phone.os}")
