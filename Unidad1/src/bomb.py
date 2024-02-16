# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
state = "DISARMED"
flag = "waitting"


def config(timer):
    if button_a.is_pressed():
        if button_b.is_pressed():
            state = "armed"
            flag = "2"
            timer = 0
        else:
            if timer > 1:
                countdown = timer - 1
            #falta serial
    elif button_b.was_pressed():
        if timer < 9:
            countdown = timer + 1
            #falta serial
    #Display
    display.show(timer)

def countdown(timer):
    #Display
    display.show(timer)

    #falta serial

    #timer
    countdown = timer - 1



while True:
    if state == "DISSARMED":
        #config timer
        config(countdown)
    elif state == "ARMED":
        countdown(countdown)
