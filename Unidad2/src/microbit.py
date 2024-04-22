from microbit import *
import music

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
        send = False
    uart_buffer = ''
        

    # Read mfp0
    if uart.any():
        display.show(Image.HAPPY)
        data = uart.readline()#uart.read(1)
        if data:
            if data[0] == ord('M'):
                music.play(music.PYTHON)
            if data[1] == ord('F'):
                music.play(['e'])
                display.scroll(data[3])
            if data[2] == ord('P'):
                music.play(['c'])
                
