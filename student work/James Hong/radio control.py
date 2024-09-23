from microbit import *
import radio
radio.config(group=23)
radio.on()

while True:
    if button_a.is_pressed():
        radio.send('left')
    if button_b.is_pressed():
        radio.send('right')
    if pin_logo.is_touched():
        radio.send('back')
    if accelerometer.was_gesture('shake'):
        radio.send('grab')
    else:
        radio.send('stop')
