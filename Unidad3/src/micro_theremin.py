# Imports go at the top
from microbit import *
import music

# Variables ---------------------------------
uart.init(baudrate=115200)
theremin_mode = 0
state = 1;
# Variables ---------------------------------

# States ------------------------------------
def state_1():
    if button_a.was_pressed():
        theremin_mode = 1
    if button_b.was_pressed():
        theremin_mode = 2

def theremin_1():
    music.set_tempo(bpm=120)

    x_strength = accelerometer.get_x()
    # x_strength *= 10
    display.scroll(x_strength)
    print(x_strength)

def theremin_2():
    music.set_tempo(bpm=120)
# States ------------------------------------
    

# Setup -------------------------------------
display.show(Image.SILLY)
# Setup -------------------------------------


# loop repeats forever ----------------------
while True:
    if state == 1: 
        state_1()
        break
    elif state == 2:
        if theremin_mode == 1:
            theremin_1()
            break
        else:
            theremin_2()
            break
# loop repeats forever ----------------------
