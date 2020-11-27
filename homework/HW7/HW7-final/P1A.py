from Markov import *

# demo
weather_today = Markov()
print("The probability that a windy day follows a cloudy day is %.4f"%weather_today.get_prob("windy", "cloudy"))
print(weather_today.get_prob("rainy", "windy")) # This line should print 0.05
print(weather_today.get_prob('sunny', 'cloudy')) # This line should print 0.3
weather_today.get_prob("a", "windy") # This line should give exception
