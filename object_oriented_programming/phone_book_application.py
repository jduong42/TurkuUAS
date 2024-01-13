def phone_book():

    print("\n Welcome to your phone book application.\n", "Choose your command to proceed.\n\n", "1. Search\n", "2. Add\n", "3. Quit.\n")

    phone_log = initialize_phone_book()
    user_input = 0

    while True:

        user_input = int(input(""))

        while user_input != 3:
            if user_input <= 0 or user_input > 3:
                print("\nWrong input. Choose a valid option.\n")
            if user_input == 1:
                search_contacts(phone_log)
                print("Choose your command to proceed.\n\n", "1. Search\n", "2. Add\n", "3. Quit.\n")
                break
            if user_input == 2:
                add_contact(phone_log)
                print("Choose your command to proceed.\n\n", "1. Search\n", "2. Add\n", "3. Quit.\n")
                break
        if user_input == 3:
            print("\nApplication is quitting...")
            break
    
    return

def initialize_phone_book():

    contacts = {
        "Person": []
    }
    
    return contacts

def add_contact(phone_log):

    print("\nPlease choose if you want to add 1. Name and number or 2. To return previous menu.")

    user_input = int(input(""))

    if user_input <= 0 or user_input > 2:
        print("\nWrong input. Choose a valid option.")
    if user_input == 1:
        name = str(input("\nPlease give a name to be added to phone log.\n"))
        number = int(input("\nPlease insert a phone number tied to the person.\n"))

        for contact in phone_log["Person"]:
            if contact["Name"] == name:
                print("\nName already exists. Choose a different name.\n")
        else:
            new_contact = {"Name": name, "Number": number}
            phone_log["Person"].append(new_contact)
    if user_input == 2:
        return phone_log

    add_contact(phone_log)

def search_contacts(phone_log):

    name = str(input("\nPlease input a name you want to search from the contacts.\n"))
    
    for contact in phone_log["Person"]:
        if contact["Name"] == name:
            print(f"Person was found in the phone log. \nName: {name}, Number: {contact["Number"]}\n")
            break
        print(f"{name} not found in phone log.\n")

    user_input = int(input("Press 1. to continue searching a name from the contacts or 2. to go to previous menu.\n"))

    if user_input == 1:
        search_contacts(phone_log)
    else:
        return

    
def main():
    phone_book()

if __name__ == "__main__":
    main()