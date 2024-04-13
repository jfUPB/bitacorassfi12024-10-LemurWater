from microbit import *

uart.init(baudrate=115200)
display.show(Image.BUTTERFLY)
uart_buffer =''

while True:
    # Pause
    if pin_logo.is_touched():
        uart_buffer = uart_buffer + 'P'
        # uart.write('P')
        
    # Accelerometer  
    if accelerometer.was_gesture('shake'):
         x_strength = accelerometer.get_x()
         uart_buffer = uart_buffer + 'X'
         # uart.write('X')
   
    # Button press
    if button_a.was_pressed():
        uart_buffer = uart_buffer + 'A'
        # uart.write('A')
    if button_b.was_pressed():
        uart_buffer = uart_buffer + 'D'
        # uart.write('D')
    
    # Send
    if len(uart_buffer) > 0:
        uart.write(uart_buffer)
        uart_buffer = ''

    # Read
    if uart.any():
        data = uart.read(1)
        if data:
            if data[0] == ord('h'):
                display.show(Image.HEART)
