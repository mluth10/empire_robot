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
    # #90 - 140, start at 120
    # hip_joint = 25 * sin(t - 3.34295) + 115
    # #170 - 70, start at 120
    # knee_joint = 50 * sin(t) + 120

    # #want same dir?
    # hip_joint_2 = -25 * sin(t - 2.94) + 115
    # knee_joint_2 = -50 * sin(t) + 120

    waves = {}
    waves[1] = 25 * sin(t - 3.34295) + 115
    waves[2] = 50 * sin(t) + 120
    waves[3] = -25 * sin(t - 2.94) + 115
    waves[4] = -50 * sin(t) + 120
    waves[7] = 25 * sin(t - 3.34295) + 115
    waves[8] = 50 * sin(t) + 120
    waves[5] = -25 * sin(t - 2.94) + 115
    waves[6] = -50 * sin(t) + 120

    for i in waves:
        motors[i].move(waves[i])

    # servo1.move(hip_joint)
    # servo2.move(knee_joint)
    # servo3.move(hip_joint_2)
    # servo4.move(knee_joint_2)

    time.sleep(0.05)
    t += 0.1

