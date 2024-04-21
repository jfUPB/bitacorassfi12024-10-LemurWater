# Imports go at the top
from microbit import *
import music
import speech

# Variables ---------------------------------
uart.init(baudrate=115200)
state = 1
octave = 1
tune = 1
# Variables ---------------------------------
# standar ---------------------------
def error_sound():
    music.play(['d', 'c'], wait=False)

def confirm_sound():
    music.play(['c', 'd'], wait=False)
# standar ---------------------------
# States ------------------------------------
def state_1_octave():
    global state
    global octave
    
    if accelerometer.was_gesture('shake'):
        state = 2
        speech.say('Select tune')
    elif button_a.was_pressed():
        if octave <= 1:
            octave = 1
            error_sound()
        else:
            octave -= 1 
            display.show(octave)
            confirm_sound()
    elif button_b.was_pressed():
        if octave >= 7:
            octave = 7
            error_sound()
        else:
            octave += 1
            display.show(octave)
            confirm_sound()

def state_2_tune():
    global state
    global tune
    _gate = False
    
    if pin_logo.is_touched():
        state = 3
    if button_a.was_pressed():
        if tune <= 1:
            tune = 12
            error_sound()
        else:
            tune -= 1
            _gate = True
            confirm_sound()
    if button_b.was_pressed():
        if tune >= 12:
            tune = 1
            error_sound()
        else:
            tune += 1
            _gate = True
            confirm_sound()
    if _gate:
        display.show(Image.HAPPY)
        if tune == 1: display.show('C')
        elif tune == 2: display.scroll('C#', wait=False)
        elif tune == 3: display.show('D')
        elif tune == 4: display.scroll('D#', wait=False)
        elif tune == 5: display.show('E')
        elif tune == 6: display.show('F')
        elif tune == 7: display.scroll('F#', wait=False)
        elif tune == 8: display.show('G')
        elif tune == 9: display.scroll('G#', wait=False)
        elif tune == 10: display.show('A')
        elif tune == 11: display.scroll('A#', wait=False)
        elif tune == 12: display.show('B')
# Play --------------------------------------
def sense_movement():
    x_strength = accelerometer.get_x()
    display.scroll(x_strength)
    music.pitch(440)
    music.play(music.WAWAWAWAA)
    
    
# Play --------------------------------------
def play():
    music.set_tempo(bpm=120)

    x_strength = accelerometer.get_x()
    # x_strength *= 10
    display.scroll(x_strength)
    print(x_strength)
# States ------------------------------------
# Setup -------------------------------------
def setup():
    display.show(Image.SILLY)
    speech.say('Select octave')
# Setup -------------------------------------

setup()
# loop repeats forever ----------------------
while True:
    if state == 1: 
        state_1_octave()
    elif state == 2:
        state_2_tune()
    elif state == 3:
        play()
# loop repeats forever ----------------------
