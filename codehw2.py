# Using a light sensor
from microbit import *
import time

while True:
    time.sleep(0.05)    # Ｔhe sensor detacts the intensity of surrounding light once in 0.05 milliseconds
    reading = pin2.read_analog()    # Read analog light values by attacheing a cable to pin2
    print((reading,))   # Open "Plotter" to get values from the light sensor while running

    if reading >= 386:  # reading higher values = environment less light
        boat = Image("99999:99999:99999:99999:99999")
        display.show(boat)

    elif reading >= 365:
        boat = Image("00000:99999:99999:99999:99999")
        display.show(boat)

    elif reading >= 350:
        boat = Image("00000:00000:99999:99999:99999")
        display.show(boat)

    elif reading >= 330:
        boat = Image("00000:00000:00000:99999:99999")
        display.show(boat)

    elif reading >= 290:
        boat = Image("00000:00000:00000:00000:99999")
        display.show(boat)

    else:
        boat = Image("03030:33333:33333:03330:00300")   #DIY dimmer Image.HEART
        display.show(boat)