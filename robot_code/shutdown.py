from math import sin, cos, pi
from pylx16a.lx16a import *
import time

LX16A.initialize("/dev/ttyUSB0") #change this, look at readme in github

initial_angles = [125, 115, 115, 110, 115, 115, 120, 120]

try:
    motors = {}
    for i in range(1,9):
        motors[i] = LX16A(i)
        motors[i].set_angle_limits(0,240)
        print(motors[i].get_physical_angle()) # query positions

        motors[i].move(angle=initial_angles[i-1], time=1000)

        if abs(motors[i].get_physical_angle - initial_angles[i-1]) > 3:
            print('motor {i} at wrong spot')
            quit()
        
        motors[i].disable_torque()


except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

except ServoLogicalError as e:
    print(f"attempting to perform invalid action on motor {e.id_}")
    quit()

