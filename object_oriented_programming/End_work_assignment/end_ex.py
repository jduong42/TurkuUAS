class Phone:    
    # Parent class for phones
    def __init__(self, brand: str, imei: int, storage_size: int, memory_size: int, screen_size: float,
                 model: str, year_of_publish: int):
        self.brand = brand
        self.imei = imei
        self.storage_size = storage_size
        self.memory_size = memory_size
        self.screen_size = screen_size
        self.model = model
        self.year_of_publish = year_of_publish

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year_of_publish})"
    
class smartPhone(Phone):    
    # Child class for smartphones
    def __init__(self, brand: str, imei: int, storage_size: int, memory_size: int, screen_size: float,
                 model: str, year_of_publish: int, os: str, sd_card_slot: bool, sim_card: bool = True):
        super().__init__(brand, imei, storage_size, memory_size, screen_size, model, year_of_publish)
        self.os = os
        self.sd_card_slot = sd_card_slot
        self.sim_card = sim_card

    def add_sd_card(self, sd_card: bool, sd_card_size: int):
        # A method is added for adding the SD card to the phone.
        if sd_card == True:
            self.storage_size += sd_card_size
            print(f"SD card was added. New storage size: {self.storage_size} Gb.")
        else:
            raise ValueError("No SD card slot available!")
        
    def remove_sd_card(self, sd_card: bool, sd_card_size: int):
        # A method is added for removing the SD card from the phone.
        if sd_card == True:
            self.storage_size -= sd_card_size
            print(f"SD card was removed. New storage size: {self.storage_size} Gb.")
        else:
            raise ValueError("No SD card slot available!")
        
    def add_sim_card(self, sim_card: bool, esim_card = False):
        # Function is adding sim card to the phone, also it can add eSIM card if it is available making the function polymorphic.
        if sim_card == True:
            if esim_card == True:
                print("eSIM card was added.")
            else:
                print("Physical SIM card was added.")
        else:
            raise ValueError("No SIM card slot available!")

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
            phones = ', '.join(str(phone) for phone in self.phone)
            return f"{self.first_name} {self.last_name} ({self.age}) is using {phones}."
        
class phoneTrade:
    def __init__(self, user: User):
        self.user = user
        self.list_available_phones = []
    
    def user_trade_phone(self, user: User, phone: Phone):
        # A method is added for trading the phone.
        self.user = user
        if phone in user.phone:
            print(f"{user.first_name} {user.last_name} is trading {phone.brand}.")
            user.phone.remove(phone)
            self.list_available_phones.append(user.phone)
            self.user.remove_phone(user.phone)
        else:
            raise ValueError("User does not have this phone.")
        
    def __str__(self):
        # A method is added for printing the trade information.
        return f"Available phones for trade: {self.list_available_phones}."
    

    
phone_1 = smartPhone("Samsung", 123456789, 128, 4, 6.5, "Galaxy S20", 2020, "Android", True)
print(phone_1)
user_1 = User("John", "Doe", 25, phone_1)
print(user_1)
user_1.set_phone(phone_1)
print(user_1)

phone_2 = smartPhone("Apple", 987654321, 256, 6, 6.1, "iPhone 11", 2019, "iOS", False)
print(phone_2)
user_1.set_phone(phone_2)
print(user_1)
user_1.remove_phone(phone_1)
print(user_1)
phoneTrade_1 = phoneTrade(user_1)
phoneTrade_1.user_trade_phone(user_1, phone_2)
print(phoneTrade_1)
