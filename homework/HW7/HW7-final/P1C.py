from Markov import *
from collections import Counter

city_weather = {
    'New York': 'rainy',
    'Chicago': 'snowy',
    'Seattle': 'rainy',
    'Boston': 'hailing',
    'Miami': 'windy',
    'Los Angeles': 'cloudy',
    'San Francisco': 'windy'
}


city_simulation_result = {}
for city in city_weather:
    mk = Markov(day_zero_weather = city_weather[city])
    city_simulation_result[city] = Counter(mk.get_weather_for_day(day = 7, trials= 100))

for city in city_simulation_result:
    print(city+": "+str(dict(city_simulation_result[city])))

print("\n")
print("Most likely weather in seven days")
print("----------------------------------")
for city in city_simulation_result:
    print(city+": "+max(city_simulation_result[city], key=city_simulation_result[city].get))

