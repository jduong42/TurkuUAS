from phone_class import Phone

class User:
    # Parent class for users
    def __init__(self, first_name: str, last_name: str, age: int, phone: Phone):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone = []

    def set_phone(self, phone: Phone):
        # A method is added for setting the phone for the user.
        self.phone.append(phone)

    def remove_phone(self, phone: Phone):
        # A method is added for removing the phone from the user.
        self.phone.remove(phone)

    def get_phone(self):
        # A method is added for checking what phones the user has or have.
        return self.phone

    def __str__(self):
        # A method is added for printing the user's information.
        if len(self.phone) == 0:
            return f"{self.first_name} {self.last_name} ({self.age}) has no phone."
        else:
            phone_str = ', '.join(str(phone) for phone in self.phone)
            return f'User({self.first_name}, {self.last_name}, {self.age}, {phone_str})'
        