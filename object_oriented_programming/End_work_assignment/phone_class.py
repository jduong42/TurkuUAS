class Phone:    
    # Parent class for phones
    def __init__(self, brand: str, model: str, year_of_publish: int):
        self.brand = brand
        self.model = model
        self.year_of_publish = year_of_publish

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year_of_publish})"
    
class smartPhone(Phone):    
    # Child class for smartphones
    def __init__(self, brand: str, model: str, year_of_publish: int, os: str, sd_card_slot: bool, sim_card: bool = True):
        super().__init__(brand, model, year_of_publish)
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
        
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year_of_publish}) - {self.os}"