from math import sin, cos, pi
from pylx16a.lx16a import *
import time

LX16A.initialize("/dev/ttyUSB0") #change this, look at readme in github

try:
    initial_angles = [125, 115, 115, 110, 115, 115, 120, 120]

    motors = {}
    for i in range(1,9):
        motors[i] = LX16A(i)
        motors[i].set_angle_limits(0,240)
        print(motors[i].get_commanded_angle()) # query positions
        motors[i].move(angle=initial_angles[i-1], time=1000) #move to start positions
        
        # if motors[i].get_temp() > 50 or motors[i].get_temp() < 10:
        #     print('either too hot or too cold')
        #     quit()

        # if abs(motors[i].get_physical_angle() - initial_angles[i-1]) > 2:
        #     print(f"motor {i} not in proper spot")

except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()
