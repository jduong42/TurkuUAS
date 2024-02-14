class WeatherStation:
    def __init__(self, name):
        self.__name = name
        self.__observation = []

    def add_observation(self, observation: str):
        self.__observation.append(observation)
    
    def latest_observation(self):
        if len(self.__observation) == 0:
            return ""
        return self.__observation[-1]
    
    def number_of_observations(self):
        return len(self.__observation)
    
    def __str__(self):
        return f"{self.name} has {self.number_of_observations()} observations."
    
    @property
    def name(self):
        return self.__name

station = WeatherStation("Houston")
station.add_observation("Rain 10mm")
station.add_observation("Sunny")
print(station.latest_observation())
station.add_observation("Thunderstorm")
print(station.latest_observation())
print(station.number_of_observations())
print(station)