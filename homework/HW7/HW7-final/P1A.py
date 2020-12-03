from Markov import *

# demo
weather_today = Markov() # actually initialization will load data automatically
weather_today.load_data(file_path='./weather.csv') # add a redundant line here for P1A requirement purpose
print("The probability that a windy day follows a cloudy day is %.4f" % weather_today.get_prob("cloudy", "windy"))
# print(weather_today.get_prob("rainy", "windy")) # This line should print 0.05
# print(weather_today.get_prob('sunny', 'cloudy')) # This line should print 0.3
# weather_today.get_prob("a", "windy") # This line should give exception
