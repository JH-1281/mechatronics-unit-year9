from microbit import *
import maqueenplus
from time import sleep_ms

mq = maqueenplus.MaqueenPlus(pin1, pin2)

MOTOR_SPEED = 35
driving = False

while True:
    if button_a.was_pressed():
        driving = True
        mq.set_headlight_rgb(mq.HEADLIGHT_BOTH, mq.COLOR_GREEN)

    if pin_logo.is_touched():
        driving = False
        mq.set_headlight_rgb(mq.HEADLIGHT_BOTH, mq.COLOR_RED)
        display.clear()

    L3, L2, L1, R1, R2, R3 = mq.line_track()
    mq.motor_run(mq.MOTOR_BOTH, mq.MOTOR_DIR_FORWARD, 10)
    
    if driving:
        display.show(Image.HAPPY)
        mq.motor_run(mq.MOTOR_LEFT, mq.MOTOR_DIR_FORWARD, 10)
        all_sensors = (L3, L2, L1, R1, R2, R3)
        
            
        # In Python you can test tuples directly, eg
        # if all_sensors == (True, True, True, True, True, True):
        #     do_something()
