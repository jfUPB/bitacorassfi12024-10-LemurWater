from microbit import *
import music
import speech
import utime
# ------------------------------------------------------------------------
DELAY_TIMER = 75
DELAY_SHORT = 400
DELAY_LONG = 1250
# ------------------------------------------------------------------------
state = 'ÍNITIALIZE'
timer
startTime
# ------------------------------------------------------------------------
sequence
sequencePtr
# ------------------------------------------------------------------------
uart.init(baudrate=115200)
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
def initialize():
    global state

    if pin0.is_touched(): 
        if pin1.is_touched(): 
            if pin2.is_touched():
                state ='SETUP'
                uart.write('1')
            else :
                display.show(Image.NO)
                sleep(2000)
        else :
            display.show(Image.NO)
            sleep(2000)
    else :
        display.show(Image.NO)
        sleep(2000)
# ------------------------------------------------------------------------
def setup():
    global state
    global dcode
    global userInput
    global userInputPtr
    global timer
    global startTime
    global sequence
    global sequencePtr

    timer = 20
    userInputPtr = 0
    startTime = utime.ticks_us()
    sequence = [[True, False, False], [False, False, True]]
    sequencePtr = 0
    state = 'CONFIGURE'
    uart.write(str('S=' + state))

    speech.say('CONFIG')
# ------------------------------------------------------------------------
def timer_increase():
    global timer

    if timer > 60:
        timer = 5
    else:
        timer = timer + 5
        uart.write(str(timer))
def timer_decrese():
    global timer

    if timer < 5:
        timer = 60
    else:
        timer = timer - 5
        uart.write(str(timer))
# ------------------------------------------------------------------------
def read():
    global state
    global timer
    
    if uart.any():
        data = uart.read(1)
        if data:
            if state == 'CONFIG':
               if data[0] == ord('+'):
                   timer_increase()
               elif data[0] == ord('-'):
                   timer_decrese()
               elif data[0] == 'S':
                   state = 'COUNTDOWN'
# ------------------------------------------------------------------------
def configure():
    global state
    global timer

    read()

    if button_a.was_pressed():
        timer_increase()
    elif button_b.was_pressed():
        state = 'COUNTDOWN'
        uart.write('2')
        speech.say('ACTIVATED')
# ------------------------------------------------------------------------
def countdown():
    global state
    global timer
    global startTime

    if utime.ticks_diff(utime.ticks_us(), startTime) > 1000000:
        startTime = utime.ticks_us()
        if timer > 0:
            timer = timer - 1
            display.scroll(str(timer), wait=False)
            if timer > 10:
                music.pitch(666, 250, wait=False)
                uart.write('Y')
            elif timer < 11 and timer > 5:
                music.pitch(777, 250, wait=False)
                uart.write('O')
            else:
                music.pitch(999, 250, wait=False)
                uart.write('R')
        else:
            state = 'EXPLODE'
            uart.write('3')
# ------------------------------------------------------------------------
def wires():
    global state
    global sequence
    global sequencePtr
    
    if sequencePtr == 0:
        if pin0.is_touched() == sequence[0][0]:
            if pin1.is_touched() == sequence[0][1]:
                if pin2.is_touched() == sequence[0][2]:
                    sequencePtr = 1;
                else:
                    return
            else:
                state = 'EXPLODE'
                uart.write('3')
        else:
            state = 'EXPLODE'
            uart.write('3')

    elif sequencePtr == 1:
        if pin0.is_touched() == sequence[1][0]:
            if pin1.is_touched() == sequence[1][1]:
                if pin2.is_touched() == sequence[1][2]:
                    sequencePtr = 2;
                else:
                    return
            else:
                state = 'EXPLODE'
                uart.write('3')
        else:
            state = 'EXPLODE'
            uart.write('3')

    elif sequencePtr == 2:
        if pin0.is_touched() == False:
            if pin1.is_touched() == False:
                if pin2.is_touched() == False:
                    state = 'DISARMED'
                    uart.write('4')
                else:
                    return
            else:
                state = 'EXPLODE'
                uart.write('3')
        else:
            state = 'EXPLODE'
            uart.write('3')
# ------------------------------------------------------------------------
def explode():
    global state
    
    music.set_tempo(bpm=110)
    display.show(Image.SKULL)
    music.play(music.FUNERAL, wait=True, loop=False)
    sleep(DELAY_LONG)
    state = 'SETUP'
    uart.write('0')
# ------------------------------------------------------------------------
def disarmed():
    global state

    display.show(Image.HAPPY)
    music.play(music.ENTERTAINER, wait=True, loop=False)
    sleep(DELAY_LONG)
    state = 'SETUP'
    uart.write('0')
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# Code in a 'while True:' loop repeats forever
while True:
    if state == 'INITIALIZE':
        initialize()
    elif state == 'SETUP':
        setup()
    elif state == 'CONFIGURE':
        configure()
    elif state == 'COUNTDOWN':
        wires()
        countdown()
    elif state == 'EXPLODE':
        explode()
    elif state == 'DISARMED':
        disarmed()
# ------------------------------------------------------------------------
