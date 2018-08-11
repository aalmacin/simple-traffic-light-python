
# 60 s / 20 s
import datetime
import time

GREEN="Green"
YELLOW="Yellow"
RED="Red"

def get_second():
    return int(round(time.time()))

initialMillis = get_second()

def get_color(color, delta, greenTime, redTime):
    if delta != 0 and color == GREEN and delta % greenTime == 0: return YELLOW
    elif color == YELLOW and delta % 3 == 0: return RED
    elif color == RED and delta % redTime == 0: return GREEN
    return color

color = GREEN
previousColor = ""

def morning_evening_seq():
    return get_color(color, delta, 60, 20)

def midday_overnight_seq():
    return get_color(color, delta, 30, 30)

while True:
    currentMillis = get_second()
    delta = currentMillis - initialMillis

    color = morning_evening_seq()
    print(color, delta)
    if previousColor != color:
        delta = 0
    previousColor = color
