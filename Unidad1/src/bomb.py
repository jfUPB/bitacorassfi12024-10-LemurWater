# Imports go at the top
from microbit import *
import music
import speech


global timer
global state


def _clear_display():
    display.show(Image('00000:'
                       '00000:'
                       '00000:'
                       '00000:'
                       '00000'))
    
    
def _draw_arrow():
    _clear_display()
    
    display.set_pixel(0,2,9)
    display.set_pixel(1,1,9)
    display.set_pixel(1,3,9)
    display.set_pixel(2,0,9)
    display.set_pixel(2,4,9)
    
    display.set_pixel(1,2,9)
    display.set_pixel(2,2,9)
    display.set_pixel(3,2,9)
    display.set_pixel(4,2,9)
    
def setup():
    global timer
    global state

    state = 'SETUP'
    speech.say('SETUP')
    timer = 9
    set_volume(128)
    _draw_arrow()
    sleep(400)
    state = 'CONFIG'
    speech.say('CONFIG')
    
    
def config():
    global timer
    global state
    
    if button_a.is_pressed() and button_b.is_pressed() or pin_logo.is_touched():
        state = 'ARMED'
        speech.say('ARMED')
    if button_a.was_pressed():
        if timer > 1:
            timer = timer - 1
            display.show(timer)
            music.play(['c'])
            #falta serial
    elif button_b.was_pressed():
        if timer < 9:
            timer = timer + 1
            display.show(timer)
            music.play(['d'])
            #falta serial

def countdown():
    global timer
    global state
    
    display.show(timer)

    #falta serial
    
    #Timer
    if timer > 0:
        timer = timer - 1
        if timer > 5:
            #music.play(['e4:4'], wait=False)
            music.pitch(666, 500, wait=False)
        elif timer < 6 and timer > 3:
            #music.set_tempo(bpm=180)
            music.pitch(666, 250, wait=True)
            music.pitch(666, 250, wait=True)
        else:
             #music.set_tempo(bpm=240)
             #music.play(['d4', 'd4', 'd4', 'd4', 'd4', 'd4'])
             music.pitch(666, 125, wait=True)
             music.pitch(666, 125, wait=True)
             music.pitch(666, 125, wait=True)
             music.pitch(666, 125, wait=True)
        sleep(1000)
    else:
        state = 'EXPLODE'
        
    if pin_logo.is_touched():
        state = 'DISARMED'
        speech.say('DISARMED')

def explode():
    global state
    
    music.set_tempo(bpm=110)
    display.show(Image.SKULL)
    state = 'SETUP'
    music.play(music.FUNERAL, wait=True, loop=False)
    sleep(400)

def player_win():
    global state
    
    display.show(Image.HEART)
    music.play(music.FUNK)
    sleep(400)
    state = 'SETUP'

def io_read():
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



setup()


# Code in a 'while True:' loop repeats forever
while True:
    if state == 'SETUP':
        setup()
    if state == 'CONFIG':
        config()
    elif state == 'ARMED':
        countdown()
    elif state == 'EXPLODE':
        explode()
    elif state == 'DISARMED':
        player_win()
