# Don't try to run this as a script or it will all be over very quickly
# it won't do any harm though.
# these are all the elements you need to control PWM on 'normal' GPIO ports
# with RPi.GPIO - requires RPi.GPIO 0.5.2a or higher

import RPi.GPIO as GPIO  # always needed with RPi.GPIO
import time
import pygame


pygame.init()
window = pygame.display.set_mode((100, 100))

exit = False
duty = 0


GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM

GPIO.setup(18, GPIO.OUT)  # set GPIO 25 as an output. You can use any GPIO port

p = GPIO.PWM(18, 5000)  # create an object p for PWM on port 25 at 50 Hertz
# you can have more than one of these, but they need
# different names for each port
# e.g. p1, p2, motor, servo1 etc.

p.start(duty)  # start the PWM on 50 percent duty cycle
# duty cycle value can be 0.0 to 100.0%, floats are OK


while True:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                duty -= 5
                if duty < 0:
                    duty = 0
                p.ChangeDutyCycle(duty)
                print(duty)
            if event.key == pygame.K_UP:
                duty += 5
                if duty > 100:
                    duty = 100
                p.ChangeDutyCycle(duty)
                print(duty)



        if event.type == pygame.QUIT:
            exit = True
            # Clear servo on GPIO17
            p.stop()  # stop the PWM output
            GPIO.cleanup()  # when your program exits, tidy up after yourself
            break

    if exit:
        break




# from RPIO import PWM
# import pygame
#
# exit = False
#
# pygame.init()
# window = pygame.display.set_mode((100, 100))
#
# servo = PWM.Servo()
#
# while True:
#     for event in pygame.event.get():
#
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_1:
#                 servo.set_servo(17, 1000)
#             if event.key == pygame.K_2:
#                 servo.set_servo(17, 5000)
#
#         if event.type == pygame.QUIT:
#             exit = True
#
#             # Clear servo on GPIO17
#             servo.stop_servo(17)
#             break
#
#     if exit:
#         break
