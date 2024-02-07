# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    if pin0.is_touched():
        display.show(0)
    else:
        display.show(1)