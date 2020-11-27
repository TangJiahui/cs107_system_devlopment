import numpy as np

ALL_WEATHERS = ["sunny", "cloudy", "rainy", "snowy", "windy", "hailing"]
WEATHER_INDICES = {v: k for (k, v) in enumerate(ALL_WEATHERS)}

class Markov:
    def __init__(self, day_zero_weather = None): # You will need to modify this header line later in Part C
        self.data = None
        self.day_zero_weather = day_zero_weather
        self.load_data()

    def load_data(self, file_path='./weather.csv'):
        self.data = np.genfromtxt(file_path,delimiter=',')

    def get_prob(self, current_day_weather, next_day_weather):
        if current_day_weather not in ALL_WEATHERS or next_day_weather not in ALL_WEATHERS:
            raise Exception("no such a weather type!")
        return self.data[WEATHER_INDICES[current_day_weather]][WEATHER_INDICES[next_day_weather]]

    def __iter__(self):
        return MarkovIterator(self, self.day_zero_weather)

    def _simulate_weather_for_day(self, day):
        if self.day_zero_weather is None or self.day_zero_weather not in ALL_WEATHERS:
            raise Exception("No day zero weather!")
        if day < 0:
            raise Exception("Day could not be less than 0")
        weather = self.day_zero_weather
        iterator = iter(self)
        for i in range(day):
            weather = next(iterator)
        return weather

    def get_weather_for_day(self, day, trials = 100):
        if trials <=0 or day <0:
            raise Exception("Day and trials should be non-negative!")
        result = []
        for i in range(trials):
            result.append(self._simulate_weather_for_day(day))
        return result

class MarkovIterator:
    def __init__(self, mk: Markov, day_zero_weather):
        self.mk = mk
        self.curr = day_zero_weather

    def __iter__(self):
        return self

    def __next__(self):
        next_day_prob = [self.mk.get_prob(self.curr, i) for i in ALL_WEATHERS]
        self.curr = np.random.choice(a = ALL_WEATHERS, p = next_day_prob)
        return self.curr
