from microbit import *
import maqueenplus
from time import sleep_ms

# Initialise the MaqueenPlus robot
# If it's successful, you should see the robot version number (1.4) scroll
# across the Microbit, and it will then show a tick
#
# Check the pins that you have your ultrasonic sensor plugged into.
# Change the pins below if you need to
mq = maqueenplus.MaqueenPlus(pin1, pin2)

START_TURNING_DISTANCE_THRESHOLD_CM = 15
MINIMUM_MOTOR_SPEED = 10
driving = False

while True:
    # Check if button A has been pressed
    if button_a.was_pressed():
        driving = True
        mq.set_headlight_rgb(mq.HEADLIGHT_BOTH, mq.COLOR_GREEN)

    # Check if the logo is being touched
    if pin_logo.is_touched():
        driving = False
        mq.set_headlight_rgb(mq.HEADLIGHT_BOTH, mq.COLOR_RED)
        display.clear()        

    range_cm = mq.get_range_cm()
    
    if driving == True:
            if range_cm <= START_TURNING_DISTANCE_THRESHOLD_CM:
                display.show(Image.SAD)
                mq.motor_run(mq.MOTOR_RIGHT, mq.MOTOR_DIR_FORWARD, MINIMUM_MOTOR_SPEED + 200)
                mq.motor_stop(mq.MOTOR_LEFT)
                
            if range_cm < 20:
                mq.motor_run(mq.MOTOR_BOTH, mq.MOTOR_DIR_FORWARD, MINIMUM_MOTOR_SPEED)
                
            if range_cm > 20:
                display.show(Image.HAPPY)
                mq.motor_run(mq.MOTOR_BOTH, mq.MOTOR_DIR_FORWARD, MINIMUM_MOTOR_SPEED + 50)


# Part 2:
#
# Now that we can safely start and stop our robot, and we've tested the
# range finding, let's start driving!
#
# If the range is less than the threshold, have the robot turn left.
# Otherwise it can drive straight ahead. Make sure to use the constant
# MOTOR_SPEED when setting the speed.
#
# Let your robot run around and see how it behaves. Does it get stuck
# sometimes? If so, can you fix it? Feel free to change the values of
# the constants and see how they affect the behaviour.
#
# Advanced:
#
# Modify the speed of the robot depending on whether there is something
# in front. When it's clear, you can go at maximum speed, but as you
# approach an obstacle, gradually slow down. Make sure to define any
# new constants you need to use.
#
# When you approach a wall, can you use trigonometry to determine the
# angle the robot is approaching the wall at? You might need to take a
# couple of measurements. Can you then make the robot move off at the
# same angle (like a bouncing ball)?
#
