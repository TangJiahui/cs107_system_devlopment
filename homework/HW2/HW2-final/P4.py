import numpy
import matplotlib.pyplot as plt
import datetime
import math

### Closure defined up here
def clock(radius):
	def coordinate(theta):
		nonlocal radius
		x = radius * math.cos(theta*math.pi/180)
		y = radius * math.sin(theta*math.pi/180)
		return x, y
	return coordinate

## Demo
currentDT = datetime.datetime.now()
hour = currentDT.hour
minute = currentDT.minute
second = currentDT.second

# Calculate theta in degrees for each hand
theta_hour = 90-30*hour-minute/2
theta_min = 90-6*minute
theta_sec = 90-6*second

# Specify the length of hour, minute and second hands
length_of_hour_hand = 7
length_of_min_hand = 12
length_of_sec_hand = 20

hour_hand = clock(length_of_hour_hand)
x_hour, y_hour = hour_hand(theta_hour)

min_hand = clock(length_of_min_hand)
x_min, y_min = min_hand(theta_min)

sec_hand = clock(length_of_sec_hand)
x_sec, y_sec = sec_hand(theta_sec)

### plot
plt.figure(figsize=(6,6))
plt.axis([-25, 25, -25, 25])
plt.plot([0, x_hour], [0, y_hour], linewidth = 10)
plt.plot([0, x_min], [0, y_min], linewidth = 7)
plt.plot([0, x_sec], [0, y_sec], linewidth = 5)
plt.show()