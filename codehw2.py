# Using a light sensor
from microbit import *
import time

while True:
    time.sleep(0.05)    # Ｔhe sensor detacts the intensity of surrounding light once in 0.05 milliseconds
    reading = pin2.read_analog()    # Read analog light values by attacheing a cable to pin2
    print((reading,))   # Open "Plotter" to get values from the light sensor while running

    if reading >= 386:  # reading higher values = environment less light
        led = Image("99999:99999:99999:99999:99999")    # Define "led" as output light
        display.show(led)

    elif reading >= 365:
        led = Image("00000:99999:99999:99999:99999")   # 0 to 9 represent the brightness levels of each LED
        display.show(led)

    elif reading >= 350:
        led = Image("00000:00000:99999:99999:99999")
        display.show(led)

    elif reading >= 330:
        led = Image("00000:00000:00000:99999:99999")
        display.show(led)

    elif reading >= 290:
        led = Image("00000:00000:00000:00000:99999")
        display.show(led)

    else:
        led = Image("03030:33333:33333:03330:00300")   #DIY dimmer Image.HEART
        display.show(led)