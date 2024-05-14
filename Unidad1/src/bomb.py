from microbit import *
import music
import speech
import utime
# ------------------------------------------------------------------------
DELAY_TIMER = 75
DELAY_SHORT = 400
DELAY_LONG = 1250
# ------------------------------------------------------------------------
state = 'INITIALIZE'
timer = 0
startTime = 0
# ------------------------------------------------------------------------
sequence = [[True, False, True], [True, False, False]]
sequencePtr = 0
# ------------------------------------------------------------------------
uart.init(baudrate=115200)
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
def initialize():
    global state

    if pin0.is_touched(): 
        if pin1.is_touched(): 
            if pin2.is_touched():
                display.show(Image.YES)
                sleep(1000)
                state ='SETUP'
                uart.write('1')
            else :
                display.show(Image.NO)
                sleep(500)
        else :
            display.show(Image.NO)
            sleep(500)
    else :
        display.show(Image.NO)
        sleep(500)
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

    timer = 5
    display.scroll(timer, wait=False)
    userInputPtr = 0
    startTime = utime.ticks_us()
    sequence = [[True, False, True], [True, False, False]]
    sequencePtr = 0
    state = 'CONFIGURE'
    uart.write('2')

    speech.say('CONFIG')
# ------------------------------------------------------------------------
def timer_increase():
    global timer

    if timer > 59:
        timer = 5
        music.play('c')
    else:
        timer = timer + 5
        if timer < 29:
            music.play('d')
        else:
            music.play('e')
    display.scroll(timer, wait=False)
def timer_decrese():
    global timer

    if timer < 5:
        timer = 60
    else:
        timer = timer - 5
        uart.write(str(timer))
def press_a():
        timer_increase()
        uart.write('+')
def press_b():
    global state
    global startTime
    
    state = 'COUNTDOWN'
    speech.say('ACTIVATED')
    music.play('f6')
    uart.write('3')
    startTime = utime.ticks_us()
# ------------------------------------------------------------------------
def read():
    global state
    global timer
    
    if uart.any():
        data = uart.read(1)
        if data:
            if state == 'CONFIGURE':
                if data[0] == ord('+'):
                    press_a()
                elif data[0] == ord('3'):
                    press_b()
# ------------------------------------------------------------------------
def configure():
    read()

    if button_a.was_pressed():
        press_a()
    elif button_b.was_pressed():
        press_b()
# ------------------------------------------------------------------------
def countdown():
    global state
    global timer
    global startTime

    if utime.ticks_diff(utime.ticks_us(), startTime) > 1000000:
        if timer > 0:
            timer = timer - 1
            startTime = utime.ticks_us()
            uart.write('t')
            display.scroll(str(timer), wait=False)
            if timer > 10:
                music.play('c6')
            elif timer < 11 and timer > 5:
                music.play('f6')
            else:
                music.play('b6')
        else:
            state = 'EXPLODE'
            uart.write('4')
# ------------------------------------------------------------------------
def wires_test():
    global state
    global sequence
    global sequencePtr
    
    if pin0.is_touched() == True:
        if pin1.is_touched() == True:
            if pin2.is_touched() == True:
                display.show(Image.HAPPY)
            else:
                display.show(Image.SAD)
        else:
            display.show(Image.SAD)
    else:
        display.show(Image.SAD)
# ------------------------------------------------------------------------
def wires():
    global state
    global sequence
    global sequencePtr

    if sequencePtr == 0:
        if pin0.is_touched() == True:
            if pin1.is_touched() == True:
                if pin2.is_touched() == True:
                    return
        if pin0.is_touched() == sequence[0][0]:
            if pin1.is_touched() == sequence[0][1]:
                if pin2.is_touched() == sequence[0][2]:
                    sequencePtr = 1;
                    uart.write('/')
                else:
                    pass
                    # state = 'EXPLODE'
                    # uart.write('3')
            else:
                pass
        else:
            pass
            # state = 'EXPLODE'
            # uart.write('3')
                
    elif sequencePtr == 1:
        if pin0.is_touched() == sequence[0][0]:
            if pin1.is_touched() == sequence[0][1]:
                if pin2.is_touched() == sequence[0][2]:
                    return

        if pin0.is_touched() == sequence[1][0]:
            if pin1.is_touched() == sequence[1][1]:
                if pin2.is_touched() == sequence[1][2]:
                    sequencePtr = 2;
                    uart.write('/')
                else:
                    pass
            else:
                pass
        else:
            pass
            # state = 'EXPLODE'
            # uart.write('4')

    elif sequencePtr == 2:
        if pin0.is_touched() == sequence[1][0]:
            if pin1.is_touched() == sequence[1][1]:
                if pin2.is_touched() == sequence[1][2]:
                    return
        if pin0.is_touched() == False:
            if pin1.is_touched() == False:
                if pin2.is_touched() == False:
                    state = 'DISARMED'
                    uart.write('5')
                else:
                    pass
                    # state = 'EXPLODE'
                    # uart.write('4')
            else:
                pass
                # state = 'EXPLODE'
                # uart.write('4')
        else:
            pass
            # state = 'EXPLODE'
            # uart.write('4')
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
