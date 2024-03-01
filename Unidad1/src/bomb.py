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

MUSIC_NOTE_A = 'c'
MUSIC_NOTE_B = 'd'

DISARM_CODE = ['UP', 'DOWN', 'UP', 'DOWN', 'UP', 'UP', 'ARMED']
userInput = ['VOID', 'VOID', 'VOID', 'VOID', 'VOID', 'VOID', 'ARMED']
userInputPtr = 0

wireMode = False
WIRE_DISARM_CODE = [1, 2, 0]# [[1, 1, 1], [1, 0, 1], [1, 0, 0], [0, 0, 0]]
#wireUserInput = [0, 0, 0]
wireDisarmPtr = 0


def _check_wires():
    if pin0.is_touched():
        wireUserInput[0] = 1
    if pin1.is_touched():
        wireUserInput[1] = 1
    if pin2.is_touched():
        wireUserInput[2] = 1
    
def _clear_input():
    if button_a.was_pressed():
        display.show(Image.HAPPY)
    if button_b.was_pressed():
        display.show(Image.HAPPY)
    
def _draw_arrow():
    display.clear()
    
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
    global wireDisarmPtr
    global wireUserInput
    global wireMode
    
    state = 'SETUP'
    set_volume(255)
    timer = 20
    userInput = ['VOID', 'VOID', 'VOID', 'VOID', 'VOID', 'VOID', 'ARMED']
    userInputPtr = 0
    startTime = utime.ticks_us()

    if _check_wires() == False: display.show(Image.NO)
    else : 
        wireDisarmPtr = 0
        wireUserInput = [0, 0, 0]
        wireMode = True
        display.show(Image.YES)

    sleep(DELAY_SHORT)
    
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
            music.play([MUSIC_NOTE_A])
            display.scroll(timer, delay=DELAY_TIMER, loop=True, wait=False)
            #falta serial
    elif button_b.is_pressed():
        if timer < 60:
            timer = timer + 1
            music.play([MUSIC_NOTE_B])
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

def input_listener():
    if wireMode == True: cable_disarm()
    else: button_disarm()

        
def button_disarm():
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
        if userInput == DISARM_CODE:
            state = 'DISARMED'
            speech.say('DISARMED')
            display.show(Image.YES)
            sleep(DELAY_TIMER)
        else:
            display.show(Image.NO)
            userInputPtr = 0


def _pin_state():
    tmp = [0, 0, 0]
    if pin0.is_touched(): tmp[0] = 1   
    if pin1.is_touched(): tmp[1] = 1  
    if pin2.is_touched(): tmp[2] = 1  
    return tmp
    
def cable_disarm():
    global wireUserInput
    global wireDisarmPtr
    global state
    
    if wireDisarmPtr == 0:
        if pin1.is_touched() == False and pin0.is_touched() == True and pin2.is_touched() == True:
            wireDisarmPtr += 1
            music.play('c')
        elif pin1.is_touched() == True and pin0.is_touched() == True or pin2.is_touched() == True:
           return
        else: state = 'EXPLODE'

    if wireDisarmPtr == 1:
        if pin0.is_touched() == True and pin1.is_touched() == False and pin2.is_touched() == True:
            wireDisarmPtr += 1
            music.play('d')
        elif pin0.is_touched() == True and pin1.is_touched() == True and pin2.is_touched() == True:
           return
        else: state = 'EXPLODE'

    if wireDisarmPtr == 2:
        if pin0.is_touched() == True and pin1.is_touched() == False and pin2.is_touched() == False:
            wireDisarmPtr += 1
            music.play('d')
        elif pin0.is_touched() == True and pin1.is_touched() == False and pin2.is_touched() == True: 
            return
        else: state = 'EXPLODE'

    if wireDisarmPtr == 3:
        if pin0.is_touched() == False and pin1.is_touched() == False and pin2.is_touched() == False:
            music.play('e')
            sleep(DELAY_SHORT)
            state = 'DISARMED'
        elif pin0.is_touched() == True and pin1.is_touched() == False and pin2.is_touched() == False: 
            return
        else: state = 'EXPLODE'


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
        
