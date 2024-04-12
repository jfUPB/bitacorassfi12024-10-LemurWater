from microbit import *

uart.init(baudrate=115200)
display.show(Image.BUTTERFLY)

while True:
    if button_a.was_pressed():
        uart.write('A')
    if button_b.was_pressed():
        uart.write('D')
    if accelerometer.was_gesture('shake'):
        uart.write('C')
    if uart.any():
        data = uart.read(1)
        if data:
            if data[0] == ord('h'):
                pass
