from phone_class import Phone, smartPhone

def ft_regular():
    brand = input("Enter phone's brand: ")
    imei = int(input("Enter phone's IMEI: "))
    storage_size = int(input("Enter phone's storage size: "))
    memory_size = int(input("Enter phone's random access memory size: "))
    screen_size = float(input("Enter phone's screen size: "))
    model = input("Enter phone's model: ")
    year_of_publish = int(input("Enter phone's year of publish: "))
    phone = Phone(brand, imei, storage_size, memory_size, screen_size, model, year_of_publish)
    return phone

def ft_smart():
    brand = input("Enter phone's brand: ")
    imei = int(input("Enter phone's IMEI: "))
    storage_size = int(input("Enter phone's storage size: "))
    memory_size = int(input("Enter phone's random access memory size: "))
    screen_size = float(input("Enter phone's screen size: "))
    model = input("Enter phone's model: ")
    year_of_publish = int(input("Enter phone's year of publish: "))
    os = input("Enter phone's operating system: ")
    sd_card_slot = bool(input("Does the phone have an SD card slot? "))
    sim_card = bool(input("Does the phone have a SIM card slot? "))
    phone = smartPhone(brand, imei, storage_size, memory_size, screen_size, model, year_of_publish, os, sd_card_slot, sim_card)
    return phone

def phone_to_user(user_list, phone_list):
    if len(user_list) == 0:
        print("No users to assign phone to.")
        return None
    if len(phone_list) == 0:
        print("No phones to assign user to.")
        return None
    print("Choose user:")
    for index, user in enumerate(user_list):
        print(f"{index + 1}. {user.first_name} {user.last_name}")
    user_input = int(input("Choose user: ")) - 1
    print("Choose phone:")
    for index, phone in enumerate(phone_list):
        print(f"{index + 1}. {phone.brand} {phone.model}")
    phone_input = int(input("Choose phone: ")) - 1
    user = user_list[user_input]
    phone = phone_list[phone_input]
    user.set_phone(phone)
    print(f"{phone.brand} {phone.model} was set for {user.first_name} {user.last_name}.")
    return user, phone