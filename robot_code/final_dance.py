from math import sin, cos, pi, floor
from pylx16a.lx16a import *
import time

LX16A.initialize("/dev/ttyUSB0")

try:
     motors = {}
     for i in range(1,9):
        motors[i] = LX16A(i)
        motors[i].set_angle_limits(0,240)
    
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

initial_angles = [125, 115, 115, 110, 115, 115, 120, 120]

# weird back feet dance
print('first back feet dance')
angle_out = 30
motors[3].move(115-angle_out, time=1000)
motors[5].move(115+angle_out, time=1000)

t = 0
while t < 100:
    waves = {}

    waves[1] = 25 * sin(t - 3.34295) + 115
    waves[2] = 50 * sin(t) + 120
    waves[3] = -25 * sin(t - 2.94) + 115
    waves[4] = -50 * sin(t) + 120
    waves[5] = 25 * sin(t - 3.34295) + 115
    waves[6] = 50 * sin(t) + 120
    waves[7] = -25 * sin(t - 2.94) + 115
    waves[8] = -50 * sin(t) + 120

    for i in waves:
        motors[i].move(waves[i])

    time.sleep(0.05)
    t += 0.1

motors[i].move(angle=initial_angles[i-1], time=1000) #move to start positions

t = 0
while t < 200:
    waves = {}
    waves[3] = 30 * sin(t) + 85
    waves[4] = 30 * sin(t) + 110
    waves[5] = -30 * sin(t) + 145
    waves[6] = -30 * sin(t) + 115

    for i in waves:
        motors[i].move(waves[i])
    
    time.sleep(0.05)
    t += 0.1

motors[i].move(angle=initial_angles[i-1], time=1000)

angle_out = 50
motors[7].move(115+angle_out, time=500)
motors[3].move(115-angle_out, time=500)
motors[5].move(115+angle_out, time=500)
motors[1].move(115-angle_out, time=500)
motors[7].move(115+angle_out, time=500)
motors[7].move(115+angle_out, time=500)
motors[7].move(115+angle_out, time=500)

time.sleep(.1)
motors[i].move(angle=initial_angles[i-1], time=1000)

angle_out = 50
motors[7].move(115+angle_out, time=500)
motors[3].move(115-angle_out, time=500)
motors[5].move(115+angle_out, time=500)
motors[1].move(115-angle_out, time=500)
motors[7].move(115+angle_out, time=500)
motors[7].move(115+angle_out, time=500)
motors[7].move(115+angle_out, time=500)

time.sleep(.1)
motors[i].move(angle=initial_angles[i-1], time=1000)

angle_out = 50
motors[7].move(115+angle_out, time=500)
motors[3].move(115-angle_out, time=500)
motors[5].move(115+angle_out, time=500)
motors[1].move(115-angle_out, time=500)
motors[7].move(115+angle_out, time=500)
motors[7].move(115+angle_out, time=500)
motors[7].move(115+angle_out, time=500)

time.sleep(.1)
motors[i].move(angle=initial_angles[i-1], time=1000)

angle_out = 20
motors[7].move(115+angle_out, time=500)
motors[3].move(115-50, time=500)
motors[5].move(115+angle_out, time=500)
motors[1].move(115-angle_out, time=500)

time.sleep(.01)
motors[4].move(80, time=500)

motors[i].move(angle=initial_angles[i-1], time=1000)

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