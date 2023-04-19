from math import sin, cos, pi
from pylx16a.lx16a import *
import time

LX16A.initialize("/dev/ttyUSB0") #change this, look at readme in github

try:
    motors = {}
    for i in range(1,9):
        motors[i] = LX16A(i)
        motors[i].set_angle_limits(0,240)
        print(motors[i].get_physical_angle()) # query positions

        # enable and disable motors
        motors[i].disable_torque()
        time.sleep(.5)
        motors[i].enable_torque()

        # get motor voltages
        print(f"motor {i} voltage: {motors[i].get_vin()}")

        #flash LEDs
        motors[i].led_power_off()
        time.sleep(.25)
        motors[i].led_power_on()
        time.sleep(.25)
        motors[i].led_power_off()
        time.sleep(.25)
        motors[i].led_power_on()
        time.sleep(.25)
        motors[i].led_power_off()
        time.sleep(.25)
        motors[i].led_power_on()

except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

except ServoLogicalError as e:
    print(f"attempting to perform invalid action on motor {e.id_}")
    quit()

