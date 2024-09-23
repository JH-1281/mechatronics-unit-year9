from microbit import *
import radio
radio.config(group=23)
import maqueenplus
radio.on()

mq = maqueenplus.MaqueenPlus(pin1, pin2)
grab = 0
while True:
    message = radio.receive()
    if message == 'left':
        mq.motor_run(mq.MOTOR_RIGHT, mq.MOTOR_DIR_FORWARD, 255)
    elif message == 'right':
        mq.motor_run(mq.MOTOR_LEFT, mq.MOTOR_DIR_FORWARD, 255)
    elif message == 'back':
        mq.motor_run(mq.MOTOR_BOTH, mq.MOTOR_DIR_BACKWARD, 255)
    elif message == 'grab':
        if grab == 0:
            mq.servo(mq.SERVO_S1, 180)
            grab = 1
        else:
            mq.servo(mq.SERVO_S1, 0)
            grab = 0
    elif message == 'stop':
        mq.motor_stop(mq.MOTOR_BOTH)
