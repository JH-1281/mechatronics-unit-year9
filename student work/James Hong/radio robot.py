from microbit import *
import radio
radio.config(group=23)
import maqueenplus
radio.on()

mq = maqueenplus.MaqueenPlus(pin1, pin2)

while True:
    message = radio.receive()
    if message == 'left':
        mq.motor_run(mq.MOTOR_RIGHT, mq.MOTOR_DIR_FORWARD, 255)
    if message == 'right':
        mq.motor_run(mq.MOTOR_LEFT, mq.MOTOR_DIR_FORWARD, 255)
    if message == 'back':
        mq.motor_run(mq.MOTOR_BOTH, mq.MOTOR_DIR_BACKWARD, 255)
    if message == 'grab':
        grab =+ 1
        if grab % 2 == 0:
            mq.servo(mq.SERVO_S1, 180)
        elif grab % 2 == 1:
            mq.servo(mq.SERVO_S1, 0)
        else:
            display.show(Image.NO)
            
    if message == 'stop':
        mq.motor_stop(mq.MOTOR_BOTH)
