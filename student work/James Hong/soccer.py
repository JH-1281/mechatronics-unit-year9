from microbit import *
import radio
import music
import maqueenplus
radio.on()
radio.config(group=23)
message = radio.receive()
mq = maqueenplus.MaqueenPlus(pin1, pin2)
grab = 0
timer = 0
colour = 0

while True:
    music.play(music.NYAN, wait=False, loop=True)
    if not message == 'stop':
        timer = running_time() + 200
        if message == 'left':
            mq.set_headlight_rgb(mq.HEADLIGHT_LEFT, mq.COLOR_RED)
            mq.set_headlight_rgb(mq.HEADLIGHT_RIGHT, mq.COLOR_WHITE)
            mq.motor_run(mq.MOTOR_RIGHT, mq.MOTOR_DIR_FORWARD, 255)
        elif message == 'right':
            mq.set_headlight_rgb(mq.HEADLIGHT_LEFT, mq.COLOR_WHITE)
            mq.set_headlight_rgb(mq.HEADLIGHT_RIGHT, mq.COLOR_RED)
            mq.motor_run(mq.MOTOR_LEFT, mq.MOTOR_DIR_FORWARD, 255)
        elif message == 'back':
            mq.set_headlight_rgb(mq.HEADLIGHT_BOTH, mq.COLOR_RED)
            mq.motor_run(mq.MOTOR_BOTH, mq.MOTOR_DIR_BACKWARD, 255)
        elif message == 'grab':
            if grab == 0:
                mq.servo(mq.SERVO_S1, 180)
                grab = 1
            else:
                mq.servo(mq.SERVO_S1, 0)
                grab = 0
    elif message == 'stop':
        mq.set_headlight_rgb(mq.HEADLIGHT_BOTH, mq.COLOR_OFF)
        mq.motor_stop(mq.MOTOR_BOTH)
        if running_time()>timer:
            timer += 200
            if colour >= 7:
               colour = 0
            headlight = [mq.COLOR_RED, mq.COLOR_YELLOW, mq.COLOR_GREEN, mq.COLOR_BLUE, mq.COLOR_CYAN, mq.COLOR_PINK]
            mq.set_headlight_rgb(mq.HEADLIGHT_BOTH, headlight[colour])
            colour += 1
