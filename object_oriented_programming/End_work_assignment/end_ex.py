class Phone:
    def __init__(self, name: str, imei: int, storage_size: int, memory_size: int, screen_size: float,
                 model: str, year_of_publish: int):
        self.name = name
        self.imei = imei
        self.storage_size = storage_size
        self.memory_size = memory_size
        self.screen_size = screen_size
        self.model = model
        self.year_of_publish = year_of_publish

    def __str__(self):
        return f"{self.name} {self.model} ({self.year_of_publish})"
    
phone_1 = Phone("Samsung", 123456789, 128, 4, 6.5, "Galaxy S20", 2020)
print(phone_1)