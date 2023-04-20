from math import sin, cos, pi, floor
from pylx16a.lx16a import *
import time


# LX16A.initialize("/dev/tty.usbserial-10") #change this, look at readme in github
LX16A.initialize("/dev/ttyUSB0")

#https://urldefense.com/v3/__https://github.com/ethanlipson/PyLX-16A/blob/master/documentation.md*lx16aget_id__;Iw!!OToaGQ!tjZu2o_4eGwUWFQVexH7vTz29dPGznkqHlsZZwaPaJf6WSH-HJuyXKYguIjeUC6NwXrOiqMz-9J8n8A$ 

try:
     motors = {}
     for i in range(1,9):
        motors[i] = LX16A(i)
        motors[i].set_angle_limits(0,240)
    
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

print(motors)

motors[3].move(148, time=500)
motors[1].move(92, time=500)






# initial_angles = [125, 115, 115, 110, 115, 115, 120, 120]

# for i in range(1,9):
#         motors[i] = LX16A(i)
#         motors[i].set_angle_limits(0,240)
#         print(motors[i].get_commanded_angle()) # query positions
#         motors[i].move(angle=initial_angles[i-1], time=1000)