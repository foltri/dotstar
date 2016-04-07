#!/usr/bin/python

# Simple strand test for Adafruit Dot Star RGB LED strip.
# This is a basic diagnostic tool, NOT a graphics demo...helps confirm
# correct wiring and tests each pixel's ability to display red, green
# and blue and to forward data down the line.  By limiting the number
# and color of LEDs, it's reasonably safe to power a couple meters off
# USB.  DON'T try that with other code!

import time
import pygame
from pygame.locals import *
import random
import sys

pygame.init()
window = pygame.display.set_mode((100, 100))

LEFT = 1
MIDDLE = 2
RIGHT = 3
SCROLL_UP = 4
SCROLL_DOWN = 5
exit = False
numpixels = (8 * 8)  # Number of LEDs in strip
numplayers = 4
playerPixelRange = numpixels // numplayers


# ##################################################
# Start of DotStar_Emulator Changed Code
#
# Wrap Adafruit DotStar import in a try/except statement and import the spoofed version if failed.  This will only
# work if the Adafruit library is not installed.  If it is installed, then just replace the Adafruit import with
# the DotStar_Emulator import
import sys


try:
    from dotstar import Adafruit_DotStar
except ImportError:
    from DotStar_Emulator import Adafruit_DotStar
# End of DotStar_Emulator Changed Code
# ##################################################



# Here's how to control the strip from any two GPIO pins:
datapin = 23
clockpin = 24
strip = Adafruit_DotStar(numpixels, datapin, clockpin)

# Alternate ways of declaring strip:
# strip   = Adafruit_DotStar(numpixels)           # Use SPI (pins 10=MOSI, 11=SCLK)
# strip   = Adafruit_DotStar(numpixels, 32000000) # SPI @ ~32 MHz
# strip   = Adafruit_DotStar()                    # SPI, No pixel buffer
# strip   = Adafruit_DotStar(32000000)            # 32 MHz SPI, no pixel buf
# See image-pov.py for explanation of no-pixel-buffer use.

strip.begin()  # Initialize pins for output
strip.setBrightness(200)  # Limit brightness to ~1/4 duty cycle

# Runs 10 LEDs at a time along strip, cycling through red, green and blue.
# This requires about 200 mA for all the 'on' pixels + 1 mA per 'off' pixel.

bgColor = 0xD68411  # 'On' color (starts red)


# def setBackground(color):
#
#     full_circle = False
#     head = 0
#     while not full_circle:
#         strip.setPixelColor(head, colorRangeRand(color,100))  # Turn on 'head' pixel
#         strip.show()  # Refresh strip
#         time.sleep(1.0 / 50)  # Pause 20 milliseconds (~50 fps)
#
#         head += 1  # Advance head position
#         if head >= numpixels:  # Off end of strip?
#             head = 0  # Reset to start
#             full_circle = True
#     return


def setBackground(color):

    setPixelRange(0,numpixels,color,delay=20)
    return


def colorRangeRand(baseColor, treshold):
    t = treshold // 2
    color = random.randint(baseColor - t, baseColor + t)
    return color


def setDelay(t):
    time.sleep(t / 1000)    #in ms


def getPlayerStartLed(player):
    return playerPixelRange * (player - 1)


def setPixelRange(start, length, color, delay=0):

    for p in range(length):
        strip.setPixelColor(start + p, color)
        if delay > 0:
            time.sleep(delay / 1000)
            strip.show()
    if delay == 0:
        strip.show()


def setPixelRange2(start, length, color, delay=0, type='fromStart'):

    if type == 'fromStart':
        for p in range(length):
            strip.setPixelColor(start + p, color)
            if delay > 0:
                setDelay(delay)
                strip.show()

    elif type == 'fromEnd':
        for p in range(length,0,-1):
            strip.setPixelColor(start + p - 1, color)
            if delay > 0:
                setDelay(delay)
                strip.show()

    elif type == 'fromCenter':
        if delay == 0: raise Exception("For type: 'fromCenter' you need to set a higher delay than 0.")
        index = length // 2
        for i in range(index):
            strip.setPixelColor(start + index + i, color)
            strip.setPixelColor(start + index - i - 1, color)
            setDelay(delay)
            strip.show()

    elif type == 'fromEnds':
        if delay == 0: raise Exception("For type: 'fromEnds' you need to set a higher delay than 0.")
        index = length // 2
        for i in range(index):
            strip.setPixelColor(start + i, color)
            strip.setPixelColor(start + length - i - 1, color)
            setDelay(delay)
            strip.show()

    if delay == 0:
        strip.show()


def gunShot(player):

    shotColor = 0
    while True:
        shotColor += 0xf0000
        start = getPlayerStartLed(player)

        if shotColor < 0xff0000:
            setPixelRange(start, playerPixelRange, shotColor)
            time.sleep(10 / 1000)
        else:
            time.sleep(50 / 1000)
            setPixelRange(start, playerPixelRange, bgColor)
            break


def gunShot2(player):

    indianColor = 0xff0000
    while True:
        start = getPlayerStartLed(player)

        setPixelRange2(start, playerPixelRange, indianColor, delay=30,  type='fromEnds')

        setDelay(400)

        setPixelRange2(start, playerPixelRange, bgColor, delay=30, type='fromEnds')
        break


def gGunShot(player):

    shotColor = 0
    while True:
        shotColor += 0xf0000

        for p in range(numplayers):
            p += 1
            if not p == player:
                start = getPlayerStartLed(player)

                if shotColor < 0xff0000:
                    setPixelRange(start, playerPixelRange, shotColor)
                    time.sleep(10 / 1000)
                else:
                    time.sleep(50 / 1000)
                    setPixelRange(start, playerPixelRange, bgColor)
                    break



def arrowShot():

    indianColor = 0xA70AC7
    while True:
        start = playerPixelRange * random.randint(0,2) + playerPixelRange // 2

        setPixelRange(start, playerPixelRange, indianColor)
        time.sleep(1000 / 1000)

        setPixelRange(start, playerPixelRange, bgColor)
        break


setBackground(bgColor)

while True:
    for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            pass

        if event.type == MOUSEBUTTONDOWN and event.button == RIGHT:
            arrowShot()

        if event.type == MOUSEBUTTONDOWN and event.button == LEFT:
            gunShot2(3)

        if event.type == MOUSEBUTTONDOWN and (event.button == SCROLL_DOWN or event.button == SCROLL_UP):
            pass

        if event.type == MOUSEBUTTONDOWN and event.button == LEFT:
            pass

        if event.type == QUIT:
            exit = True
            break

    if exit: break

