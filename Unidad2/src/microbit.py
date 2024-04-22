from microbit import *
import music

uart.init(baudrate=115200)
display.show(Image.SAD)

uart_buffer =''
BUFFER_SIZE = 256
buffer = bytearray(BUFFER_SIZE)
end = 0
send = False
questionCounter = 0

while True:
    questionCounter++
    if questionCounter == 20:
        uart.write("Q\n")
        questionCounter = 0
    if uart.any():
        display.show(Image.HAPPY)
        data = uart.readline()
        if data:
            if data[0] == ord('Q'):
                uart_buffer = ''
                if accelerometer.was_gesture('shake'):
                    uart_buffer = uart_buffer + 'P'
                    # send = True
                else: uart_buffer = uart_buffer + 'p' 
                    
                # Button press
                if button_a.was_pressed():
                    uart_buffer = uart_buffer + 'A'
                    send = True
                else : uart_buffer = uart_buffer + 'a'
                
                if button_b.was_pressed():
                    uart_buffer = uart_buffer + 'D'
                    send = True
                else : uart_buffer = uart_buffer + 'd'
                uart.write(uart_buffer)
            else:
                if data[0] == ord('M'):
                    music.play(['e'],wait=False)
                if data[1] == ord('F'):
                    display.scroll(data[2])

                
