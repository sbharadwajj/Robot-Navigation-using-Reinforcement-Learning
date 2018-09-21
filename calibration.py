# Imports
import sys
import time
import Adafruit_PCA9685

# PWM Setup
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

# Global Constants
CAL = [
    [175, 350],
    [500, 250],
    [405, 245],
    [270, 470],
    [420, 200],
    [435, 253],
    [130, 310],
    [155, 340],
    [115, 277],
    [160, 330],
    [150, 330],
    [185, 400]
]

# Global Function definitions
def set_angle(motor, angle):
    if motor < 12 or motor >=0:
        min_val = CAL[motor][0]
        max_val = CAL[motor][1]
        angle_val = min_val + (angle * (max_val - min_val) / 90)
        # print(motor, angle_val)
        pwm.set_pwm(motor, 0, int(angle_val))
        
def set_pwm(motor, pwm_val):
    pwm.set_pwm(motor, 0, pwm_val)

def stop_all():
    pwm.set_pwm(0, 0, 0), pwm.set_pwm(3, 0, 0), pwm.set_pwm(6, 0, 0), pwm.set_pwm(9, 0, 0)
    pwm.set_pwm(1, 0, 0), pwm.set_pwm(4, 0, 0), pwm.set_pwm(7, 0, 0), pwm.set_pwm(10, 0, 0)
    pwm.set_pwm(2, 0, 0), pwm.set_pwm(5, 0, 0), pwm.set_pwm(8, 0, 0), pwm.set_pwm(11, 0, 0)

def stand():
    set_angle(0,45), set_angle(3,45), set_angle(6,45), set_angle(9,45)
    set_angle(1,10), set_angle(4,10), set_angle(7,10), set_angle(10,10)
    set_angle(2,0), set_angle(5,0), set_angle(8,0), set_angle(11,0)

def sit():
    set_angle(0,45), set_angle(3,45), set_angle(6,45), set_angle(9,45)
    set_angle(1,0), set_angle(4,0), set_angle(7,0), set_angle(10,0)
    set_angle(2,90), set_angle(5,90), set_angle(8,90), set_angle(11,90)

def set_state(leg, state):
    if leg % 2 == 0:
        set_angle(leg * 3, 90 * state[0])
    else:
        set_angle(leg * 3, 90 - (90 * state[0]))

    if state[1] == 0:
        set_angle((leg * 3) + 1, -20)
        set_angle((leg * 3) + 2, 10)
    else:
        set_angle((leg * 3) + 1, 10)
        set_angle((leg * 3) + 2, 10)

def step(direction):
    w_time = 0.1
    low_a = 0
    high_a = 90
    time.sleep(w_time)
    if direction == "front":

        # set_angle(1,-20), time.sleep(w_time), set_angle(0, low_a), time.sleep(w_time), set_angle(1,10) #1
        # set_angle(10,-20), time.sleep(w_time), set_angle(9, high_a), time.sleep(w_time), set_angle(10,10) #4
        # time.sleep(w_time), set_angle(0,80), set_angle(9,10) #bring forward
        # set_angle(4,-20), time.sleep(w_time), set_angle(3, high_a), time.sleep(w_time), set_angle(4,10) #2
        # set_angle(7,-20), time.sleep(w_time), set_angle(6, low_a), time.sleep(w_time), set_angle(7,10) #3
        # time.sleep(w_time), set_angle(0,45), set_angle(3,45), set_angle(6,45), set_angle(9,45) #bring forward

        set_state(0, [0.5, 0]), time.sleep(w_time), set_state(0, [0, 0]), time.sleep(w_time), set_state(0, [0, 1]), time.sleep(w_time) #1
        set_state(3, [0.5, 0]), time.sleep(w_time), set_state(3, [0, 0]), time.sleep(w_time), set_state(3, [0, 1]), time.sleep(w_time) #4
        set_state(0, [0.5, 1]), set_state(3, [0.5, 1]), time.sleep(w_time)
        set_state(1, [0.5, 0]), time.sleep(w_time), set_state(1, [0, 0]), time.sleep(w_time), set_state(1, [0, 1]), time.sleep(w_time) #2
        set_state(2, [0.5, 0]), time.sleep(w_time), set_state(2, [0, 0]), time.sleep(w_time), set_state(2, [0, 1]), time.sleep(w_time) #3
        set_state(1, [0.5, 1]), set_state(2, [0.5, 1]), time.sleep(w_time)

       
    elif direction == "fswim":
        set_state(0, [0.5, 0]), time.sleep(w_time), set_state(0, [0, 0]), time.sleep(w_time), set_state(0, [0, 1]), time.sleep(w_time)#1
        set_state(1, [0.5, 0]), time.sleep(w_time), set_state(1, [0, 0]), time.sleep(w_time), set_state(1, [0, 1]), time.sleep(w_time)#2
        set_state(2, [0.5, 0]), time.sleep(w_time), set_state(2, [0, 0]), time.sleep(w_time), set_state(2, [0, 1]), time.sleep(w_time)#3
        set_state(3, [0.5, 0]), time.sleep(w_time), set_state(3, [0, 0]), time.sleep(w_time), set_state(3, [0, 1]), time.sleep(w_time)#4
        set_state(0, [0.5, 1]), set_state(1, [0.5, 1]), set_state(2, [0.5, 1]), set_state(3, [0.5, 1]), time.sleep(w_time)
    
    elif direction == "back":
        set_state(0, [0.5, 0]), time.sleep(w_time), set_state(0, [1, 0]), time.sleep(w_time), set_state(0, [1, 1]), time.sleep(w_time) #1
        set_state(3, [0.5, 0]), time.sleep(w_time), set_state(3, [1, 0]), time.sleep(w_time), set_state(3, [1, 1]), time.sleep(w_time) #4
        set_state(0, [0.5, 1]), set_state(3, [0.5, 1]), time.sleep(w_time)
        set_state(1, [0.5, 0]), time.sleep(w_time), set_state(1, [1, 0]), time.sleep(w_time), set_state(1, [1, 1]), time.sleep(w_time) #2
        set_state(2, [0.5, 0]), time.sleep(w_time), set_state(2, [1, 0]), time.sleep(w_time), set_state(2, [1, 1]), time.sleep(w_time) #3
        set_state(1, [0.5, 1]), set_state(2, [0.5, 1]), time.sleep(w_time)

    elif direction == "bswim":
        set_state(0, [0.5, 0]), time.sleep(w_time), set_state(0, [1, 0]), time.sleep(w_time), set_state(0, [1, 1]), time.sleep(w_time)#1
        set_state(1, [0.5, 0]), time.sleep(w_time), set_state(1, [1, 0]), time.sleep(w_time), set_state(1, [1, 1]), time.sleep(w_time)#2
        set_state(2, [0.5, 0]), time.sleep(w_time), set_state(2, [1, 0]), time.sleep(w_time), set_state(2, [1, 1]), time.sleep(w_time)#3
        set_state(3, [0.5, 0]), time.sleep(w_time), set_state(3, [1, 0]), time.sleep(w_time), set_state(3, [1, 1]), time.sleep(w_time)#4
        set_state(0, [0.5, 1]), set_state(1, [0.5, 1]), set_state(2, [0.5, 1]), set_state(3, [0.5, 1]), time.sleep(w_time)

    


        

def turn(direrction):
    w_time = 1
    if direrction == "left":
        set_state(0, [0, 0]), set_state(1, [1, 0]), set_state(2, [0, 0]), set_state(3, [1, 0]), time.sleep(w_time)
        set_state(0, [1, 0]), set_state(1, [0, 0]), set_state(2, [1, 0]), set_state(3, [0, 0]), time.sleep(w_time)
        set_state(0, [1, 1]), set_state(1, [0, 1]), set_state(2, [1, 1]), set_state(3, [0, 1]), time.sleep(w_time)
        set_state(0, [0, 1]), set_state(1, [1, 1]), set_state(2, [0, 1]), set_state(3, [1, 1]), time.sleep(w_time)
        # set_state(0, [0.5, 1]), set_state(1, [0.5, 1]), set_state(2, [0.5, 1]), set_state(3, [0.5, 1]), time.sleep(w_time)
        
    else:
        set_state(0, [1, 0]), set_state(1, [0, 0]), set_state(2, [1, 0]), set_state(3, [0, 0]), time.sleep(w_time)
        set_state(0, [0, 0]), set_state(1, [1, 0]), set_state(2, [0, 0]), set_state(3, [1, 0]), time.sleep(w_time)
        set_state(0, [0, 1]), set_state(1, [1, 1]), set_state(2, [0, 1]), set_state(3, [1, 1]), time.sleep(w_time)
        set_state(0, [1, 1]), set_state(1, [0, 1]), set_state(2, [1, 1]), set_state(3, [0, 1]), time.sleep(w_time)
        
def shutdown():
    w_time = 0.1
    sit()
    time.sleep(1)
    set_state(0, [0, 0]), time.sleep(w_time), set_state(1, [1, 0]), time.sleep(w_time), set_state(2, [0, 0]), time.sleep(w_time), set_state(3, [1, 0])#1
    time.sleep(1)
    stop_all()
try: 
    print("1 - sit\n2 - stand\n3 - frontwalk\n4 - right turn\n5 - left turn\n6 - backwalk\n7 - frontswim\n8 - backswim\n9 - sleep\n0 - shutdown\n")
    while True:
        movement, count = raw_input().split()
        ans = int(movement)
        for i in range (0, int(count)):
            pass
            if ans == 1:
                sit()
            elif ans == 2:
                stand()
            elif ans == 3:
                step("front")
            elif ans == 4:
                turn("right")
            elif ans == 5:
                turn("left")
            elif ans == 6:
                step("back")
            elif ans == 7:
                step("fswim")
            elif ans == 8:
                step("bswim")
            elif ans == 9:
                stop_all()
            elif ans == 0:
                shutdown()
                sys.exit()
            else:
                print("Invalid Input. Please input a valid option.\n")


except KeyboardInterrupt:
    stop_all()
    print("Exited\n")