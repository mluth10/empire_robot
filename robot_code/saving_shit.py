# weird back feet dance
angle_out = 30
motors[3].move(115-angle_out, time=1000)
motors[5].move(115+angle_out, time=1000)

t = 0
print("starting loop")
while True:
    waves = {}
    #waves[3] = 30 * sin(t) + 85
    waves[4] = 50 * sin(t) + 110
    #waves[5] = -30 * sin(t) + 145
    waves[6] = -50 * sin(t) + 115


# more weird back feet dance
t = 0
print("starting loop")
while True:
    waves = {}
    waves[3] = 30 * sin(t) + 85
    waves[4] = 30 * sin(t) + 110
    waves[5] = -30 * sin(t) + 145
    waves[6] = -30 * sin(t) + 115

    for i in waves:
        motors[i].move(waves[i])
    
    time.sleep(0.05)
    t += 0.1

# splits
angle_out = 50
motors[7].move(115+angle_out, time=500)
motors[3].move(115-angle_out, time=500)
motors[5].move(115+angle_out, time=500)
motors[1].move(115-angle_out, time=500)
motors[7].move(115+angle_out, time=500)
motors[7].move(115+angle_out, time=500)
motors[7].move(115+angle_out, time=500)

# twerk
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

# kick out
angle_out = 20
motors[7].move(115+angle_out, time=500)
motors[3].move(115-50, time=500)
motors[5].move(115+angle_out, time=500)
motors[1].move(115-angle_out, time=500)
time.sleep(.01)
motors[4].move(80, time=500)