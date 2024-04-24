from microbit import *
import music

uart.init(baudrate=115200)

while True:
    if uart.any():
        data = uart.readline()
        if data:
            if data[0] == ord('q'):
                message = str(accelerometer.get_x())
                message += ',' + str(accelerometer.get_y())
                uart.write(message)
