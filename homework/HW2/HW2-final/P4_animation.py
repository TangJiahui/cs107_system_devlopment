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

## breakout criteria
initial = datetime.datetime.now()
end = initial + datetime.timedelta(seconds = 30)

## constant
length_of_hour_hand = 7
length_of_min_hand = 12
length_of_sec_hand = 20
hour_hand = clock(length_of_hour_hand)
min_hand = clock(length_of_min_hand)
sec_hand = clock(length_of_sec_hand)

plt.figure(figsize=(6,6))

while datetime.datetime.now() < end:
    currentDT = datetime.datetime.now()
    ## plot current clock
    hour = currentDT.hour
    minute = currentDT.minute
    second = currentDT.second
    # Calculate theta in degrees for each hand
    theta_hour = 90-30*hour-minute/2
    theta_min = 90-6*minute
    theta_sec = 90-6*second
    x_hour, y_hour = hour_hand(theta_hour)
    x_min, y_min = min_hand(theta_min)
    x_sec, y_sec = sec_hand(theta_sec)
    plt.axis([-25, 25, -25, 25])
    plt.plot([0, x_hour], [0, y_hour], linewidth=10)
    plt.plot([0, x_min], [0, y_min], linewidth=7)
    plt.plot([0, x_sec], [0, y_sec], linewidth=5)
    plt.pause(0.1)
    plt.cla()