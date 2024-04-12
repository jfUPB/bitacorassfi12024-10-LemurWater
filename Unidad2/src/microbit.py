from microbit import *

uart.init(baudrate=115200)
display.show(Image.BUTTERFLY)

while True:
    # Send
    if button_a.was_pressed():
        uart.write('A')
    if button_b.was_pressed():
        uart.write('D')
    # Read
    if uart.any():
        data = uart.read(1)
        if data:
            if data[0] == ord('h'):
                display.show(Image.HEART)
        
    # Pause
    if pin_logo.is_touched():
        uart.write('P')
        
    # Speed  
    if accelerometer.was_gesture('shake'):
         x_strength = accelerometer.get_x()
         uart.write('X')
