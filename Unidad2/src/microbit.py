from microbit import *

uart.init(baudrate=115200)
display.show(Image.SAD)

uart_buffer =''
BUFFER_SIZE = 256
buffer = bytearray(BUFFER_SIZE)
end = 0
send = False


while True:
    # Pause
    if pin_logo.is_touched(): 
        uart_buffer = 'P'
        # send = True
    else : uart_buffer = 'p'
        
    # Accelerometer  
    if accelerometer.was_gesture('shake'):
        uart_buffer = uart_buffer + 'X'
        # send = True
    else: uart_buffer = uart_buffer + 'x'   
    
   
    # Button press
    if button_a.was_pressed():
        uart_buffer = uart_buffer + 'A'
        send = True
    else : uart_buffer = uart_buffer + 'a'
    
    if button_b.was_pressed():
        uart_buffer = uart_buffer + 'D'
        send = True
    else : uart_buffer = uart_buffer + 'd'


    
    # Send
    if send == True:
        uart.write(uart_buffer)
        uart_buffer = ''
        send = False
        

    # Read
    if uart.any():
        display.show(Image.HAPPY)
        data = uart.read(1)
        if data:
            if data[0] == ord('h'):
                display.show(Image.HAPPY)
                
            #if data[0] == ord('\n'):
            #   v end = 0
            #else:
             #   buffer[end] = data[0]
             #   end +=1
