# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
countdown = 9
state = "waitting"

while True:
    #Config
    if button_a.was_pressed():
        if countdown > 1:
            countdown = countdown -1

    elif button_b.was_pressed():
        if countdown < 9:
            countdown = countdown +1

    #Display
    display.show(countdown)