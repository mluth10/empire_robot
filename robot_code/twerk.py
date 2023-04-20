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


t = 0
print("starting loop")
while True:
    waves = {}
    #waves[3] = 30 * sin(t) + 85
    waves[4] = 40 * sin(t) + 110
    #waves[5] = -30 * sin(t) + 145
    waves[6] = -40 * sin(t) + 115

    for i in waves:
        motors[i].move(waves[i])
    
    time.sleep(0.02)
    t += 0.2
