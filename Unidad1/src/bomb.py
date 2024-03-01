# Imports go at the top
from microbit import *
import music
import speech
import utime


state = 'SETUP'
timer =  20
startTime = utime.ticks_us()
DELAY_TIMER = 75
DELAY_SHORT = 400
DELAY_LONG = 1250

dcode = ['UP', 'DOWN', 'UP', 'DOWN', 'UP', 'UP', 'ARMED']
userInput = ['ARMED', 'ARMED', 'ARMED', 'ARMED', 'ARMED', 'ARMED', 'ARMED']
userInputPtr = 0

cableCode = ["RED", "GREEN", "YELLOW"]
cableInput = ["RED", "YELLOW", "GREEN"]
cableCodePtr = 0


def _clear_input():
    if button_a.was_pressed():
        display.show(Image.HAPPY)
    if button_b.was_pressed():
        display.show(Image.HAPPY)
    
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
    global state
    global dcode
    global userInput
    global userInputPtr
    global timer
    global startTime
    
    state = 'SETUP'
    set_volume(255)
    timer = 20
    userInput = ['ARMED', 'ARMED', 'ARMED', 'ARMED', 'ARMED', 'ARMED', 'ARMED']
    userInputPtr = 0
    startTime = utime.ticks_us()
    _draw_arrow()
    state = 'CONFIG'
    speech.say('CONFIG')


def config():
    global state
    global timer
    global startTime

    if button_a.is_pressed() and button_b.is_pressed() or pin_logo.is_touched():
        state = 'ARMED'
        speech.say('ARMED')
        startTime = utime.ticks_us()
        _clear_input()
        display.scroll(timer, delay=DELAY_TIMER, loop=False, wait=False)
        sleep(DELAY_LONG)
        display.show(userInputPtr)
        sleep(DELAY_SHORT)
        return
    if button_a.is_pressed():
        if timer > 10:
            timer = timer - 1
            music.play(['c'])
            display.scroll(timer, delay=DELAY_TIMER, loop=True, wait=False)
            #falta serial
    elif button_b.is_pressed():
        if timer < 60:
            timer = timer + 1
            music.play(['d'])
            display.scroll(timer, delay=DELAY_TIMER, loop=True, wait=False)
            #falta serial



def countdown():
    global state
    global timer
    global startTime
    
    if utime.ticks_diff(utime.ticks_us(), startTime) > 1000000:
        if timer > 0:
            timer = timer - 1
            if timer > 10:
                music.pitch(666, 250, wait=False)
            elif timer < 11 and timer > 5:
                music.pitch(777, 250, wait=False)
            else:
                 music.pitch(999, 250, wait=False)
        else:
            state = 'EXPLODE'
            
        startTime = utime.ticks_us()
        display.scroll(timer, delay=DELAY_TIMER, loop=False, wait=False)

def explode():
    global state

    music.set_tempo(bpm=110)
    display.show(Image.SKULL)
    music.play(music.FUNERAL, wait=True, loop=False)
    sleep(DELAY_LONG)
    state = 'SETUP'

def disarmed():
    global state
    
    display.show(Image.HAPPY)
    music.play(music.ENTERTAINER, wait=True, loop=False)
    sleep(DELAY_LONG)
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

def input_listener():
    user_input()
    #cable_disarm()3.
        
def user_input():
    global userInputPtr
    global state
    
    if button_a.was_pressed():
        userInput[userInputPtr] = 'DOWN'
        userInputPtr += 1
        display.show(userInputPtr)
            
    elif button_b.was_pressed():
        userInput[userInputPtr] = 'UP'
        userInputPtr += 1
        display.show(userInputPtr)
            
    elif pin_logo.is_touched():
        userInput[userInputPtr] = 'ARMED'
        userInputPtr += 1
        display.show('A')

    if userInputPtr > 6:
        if userInput == dcode:
            state = 'DISARMED'
            speech.say('DISARMED')
            display.show(Image.YES)
            sleep(DELAY_TIMER)
        else:
            display.show(Image.NO)
            userInputPtr = 0
        
def cable_disarm():
    global userInputPtr
    
    if pin0.is_touched():
        userInput[userInputPtr] = 'RED'
        userInputPtr += 1
    elif pin1.is_touched():
        userInput[userInputPtr] = 'GREEN'
        userInputPtr += 1
    elif pin2.is_touched():
        userInput[userInputPtr] = 'YELLOW'
        userInputPtr += 1


# Code in a 'while True:' loop repeats forever
while True:
    if state == 'SETUP':
        setup()
    elif state == 'CONFIG':
        config()
    elif state == 'ARMED':
        countdown()
        input_listener()
    elif state == 'EXPLODE':
        explode()
    elif state == 'DISARMED':
        disarmed()
        
