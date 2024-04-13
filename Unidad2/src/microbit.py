from microbit import *

uart.init(baudrate=115200)
display.show(Image.SAD)

uart_buffer =''
BUFFER_SIZE = 256
buffer = bytearray(BUFFER_SIZE)
end = 0


while True:
    # Pause
    if pin_logo.is_touched(): uart_buffer = 'P'
    else : uart_buffer = 'p'
        
    # Accelerometer  
    if accelerometer.was_gesture('shake'): uart_buffer = uart_buffer + 'X'
    else: uart_buffer = uart_buffer + 'x'   
    
   
    # Button press
    if button_a.was_pressed(): uart_buffer = uart_buffer + 'A'
    else : uart_buffer = uart_buffer + 'a'
    
    if button_b.was_pressed(): uart_buffer = uart_buffer + 'D'
    else : uart_buffer = uart_buffer + 'd'


    
    # Send
    uart.write(uart_buffer)
    uart_buffer = ''
        

    # Read
    if uart.any():
        data = uart.read(1)
        if data:
            display.show(Image.HAPPY)
            if data[0] == ord('\n'):
                end = 0
            else:
                buffer[end] = data[0]
                end +=1
