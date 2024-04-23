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
    questionCounter+= 1
    if questionCounter == 20:
        #uart.write("Q")
        questionCounter = 0
    if uart.any():
        display.show(Image.HAPPY)
        data = uart.readline()
        if data:
            if data[0] == ord('Q'):
                #if accelerometer.was_gesture('shake'):
                #    uart.write('P')
                    
                # Button press
                if button_a.was_pressed():
                    uart.write('A')
                
                if button_b.was_pressed():
                    uart.write('B')

                
