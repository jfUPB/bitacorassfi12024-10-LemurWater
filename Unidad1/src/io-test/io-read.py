# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    if pin0.is_touched():
        if pin1.is_touched():
            display.show(2)
        else:
            display.show(3)
    else:
        if pin1.is_touched():
            display.show(1)
        else:
            display.show(0)
