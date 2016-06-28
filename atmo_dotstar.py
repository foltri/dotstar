from __future__ import division

import os
import time
import random
import numpy

try:
    from dotstar import Adafruit_DotStar
except ImportError:
    from DotStar_Emulator import Adafruit_DotStar

bgColor = 0xD68411  # 'On' color (starts red)
bgColor = 0xD17A00
bgColor = 0xFF7A00
bgColor = 0xdf6c00
bgColor = 0x913600
bgColor = 0xec6100
BRIGHTNESS = 200

numpixels = 144  # Number of LEDs in strip
numplayers = 4
playerPixelRange = numpixels // numplayers

# Here's how to control the strip from any two GPIO pins:
datapin = 23
clockpin = 24
strip = Adafruit_DotStar(numpixels, datapin, clockpin, order='bgr')

def setBackground(color, delay=10):
    setPixelRange([0], numpixels, color, delay=delay)
    return

def flash():
    strip.setBrightness(50)
    strip.show()
    setDelay(20)
    strip.setBrightness(255)
    strip.show()
    setDelay(20)
    strip.setBrightness(BRIGHTNESS)
    strip.show()
    return


def colorRangeRand(baseColor, treshold):
    t = treshold // 2
    color = random.randint(baseColor - t, baseColor + t)
    return color


def setDelay(t):
    time.sleep(t / 1000)  # in ms


def getPlayerStartLed(player):
    return playerPixelRange * (player - 1)


def setPixelRange(starts, length, color, delay=0, type='fromStart'):

    if type == 'fromStart':
        for p in range(length):
            for start in starts:
                pos = start + p
                if pos > (numpixels - 1):
                    pos -= (numpixels - 1)

                strip.setPixelColor(pos, color)
            if delay > 0:
                setDelay(delay)
                strip.show()

    elif type == 'fromEnd':
        for p in range(length, 0, -1):
            for start in starts:
                strip.setPixelColor(start + p - 1, color)
            if delay > 0:
                setDelay(delay)
                strip.show()

    elif type == 'fromCenter':
        if delay == 0: raise Exception("For type: 'fromCenter' you need to set a higher delay than 0.")
        index = length // 2
        for i in range(index):
            for start in starts:
                pos1 = start + index + i
                if pos1 > (numpixels - 1):
                    pos1 -= (numpixels - 1)
                elif pos1 < 0:
                    pos1 += (numpixels - 1)

                pos2 = start + index - i - 1
                if pos2 > (numpixels - 1):
                    pos2 -= (numpixels - 1)
                elif pos2 < 0:
                    pos2 += (numpixels - 1)


                strip.setPixelColor(pos1, color)
                strip.setPixelColor(pos2, color)
            if delay > 0:
                setDelay(delay)
                strip.show()

    elif type == 'fromEnds':
        if delay == 0: raise Exception("For type: 'fromEnds' you need to set a higher delay than 0.")
        index = length // 2
        for i in range(index):
            for start in starts:
                pos1 = start + i
                if pos1 > (numpixels - 1):
                    pos1 -= (numpixels - 1)
                elif pos1 < 0:
                    pos1 += (numpixels - 1)

                pos2 = start + length - i - 1
                if pos2 > (numpixels - 1):
                    pos2 -= (numpixels - 1)
                elif pos2 < 0:
                    pos2 += (numpixels - 1)


                strip.setPixelColor(pos1, color)
                strip.setPixelColor(pos2, color)
            if delay > 0:
                setDelay(delay)
                strip.show()

    if delay == 0:
        strip.show()


def gunShot2(player):
    shotColor = bgColor # 0xdf6c00
    start = getPlayerStartLed(player)
    on = True
    state = 0
    while on:
        print(format(shotColor,'02x'))
        if state == 0:
            shotColor -= 0x000500
            setPixelRange([start], playerPixelRange, shotColor)
            if shotColor < ((bgColor & 0xff0000) + 0x000500): state = 1
            setDelay(20)
        if state == 1:
            shotColor += 0x050000
            setPixelRange([start], playerPixelRange, shotColor)
            if shotColor & 0xff0000 == 0x00ff0000: state = 2
            setDelay(20)
        if state == 2:
            shotColor -= 0x050000
            if (shotColor & 0xff0000) < (bgColor & 0xff0000):
                shotColor = bgColor & 0xff0000
                state = 3
            setPixelRange([start], playerPixelRange, shotColor)
            setDelay(20)
        if state == 3:
            shotColor += 0x000500
            setPixelRange([start], playerPixelRange, shotColor)
            if shotColor == bgColor: on = False
            setDelay(20)
    return

def getRed(color):
    return color & 0xff0000

def getGreen(color):
    return color & 0x00ff00

def getBlue(color):
    return color & 0x0000ff

def setRGB(red,green,blue):
    r = hex(red).split('x')[1]
    if len(r) == 1: r = '0' + r
    g = hex(green).split('x')[1]
    if len(g) == 1: g = '0' + g
    b = hex(blue).split('x')[1]
    if len(b) == 1: b = '0' + b
    return int(r + g + b, 16)

# def setRed(color, red):
#     tmp1 = color & 0xff0000
#     tmp2 = color & 0x00ffff
#     newRed = tmp1 + red
#     if newRed > 0xff0000:
#         overFlow = newRed - 0xff0000
#         return overFlow + tmp2
#     if newRed < 0:
#         overFlow = newRed - 0xff0000
#         return overFlow + tmp2 ????




def gunShot(player):
    bloodColor = 0xff0000
    start = getPlayerStartLed(player)

    os.system('mpg123 -q testimages/shotgun-old_school-RA_The_Sun_God-1129942741.mp3 &')
    setDelay(50)
    flash()
    setDelay(100)

    setPixelRange([start], playerPixelRange, bloodColor, delay=5, type='fromCenter')
    setDelay(400)
    setPixelRange([start], playerPixelRange, bgColor, delay=90, type='fromEnds')
    return

def gGunShot(player):
    bloodColor = 0xff0000
    starts = []

    for p in range(numplayers):
        if not p + 1 == player:
            starts.append(getPlayerStartLed(p + 1))
    os.system('mpg123 -q testimages/shotgun-old_school-RA_The_Sun_God-1129942741.mp3 &')
    flash()
    setDelay(200)
    os.system('mpg123 -q testimages/shotgun-old_school-RA_The_Sun_God-1129942741.mp3 &')
    flash()
    setDelay(200)
    os.system('mpg123 -q testimages/shotgun-old_school-RA_The_Sun_God-1129942741.mp3 &')
    flash()
    setDelay(200)


    setPixelRange(starts, playerPixelRange, bloodColor, delay=5, type='fromCenter')
    setDelay(300)
    setPixelRange(starts, playerPixelRange, bgColor, delay=60, type='fromEnds')

    return


def gGunShot2(player):
    shotColor = 0
    while True:
        shotColor -= 0x000100

        for p in range(numplayers):
            p += 1
            if not p == player:
                start = getPlayerStartLed(player)

                if shotColor > 0xdf0000:
                    setPixelRange([start], playerPixelRange, shotColor)
                    setDelay(10)
                else:
                    setDelay(50)
                    setPixelRange([start], playerPixelRange, bgColor)
                    break


# def arrowShot():
#     indianColor = 0xd628da
#
#     # start = playerPixelRange * random.randint(0, 2) + playerPixelRange // 2
#     start = playerPixelRange * 2 + playerPixelRange // 2
#
#     os.system('mpg123 -q testimages/indian_scream2.mp3 &')
#     setPixelRange([start], playerPixelRange, indianColor, delay=15, type='fromCenter')
#     setDelay(1500)
#
#     setPixelRange([start], playerPixelRange, bgColor,delay=15,type='fromEnds')

def arrowShot(player):
    indianColor = 0xd628da

    # start = playerPixelRange * random.randint(0, 2) + playerPixelRange // 2
    start = playerPixelRange * player + playerPixelRange // 2

    os.system('mpg123 -q testimages/indian_scream2.mp3 &')
    setPixelRange([start], playerPixelRange, indianColor, delay=15, type='fromCenter')
    setDelay(1500)

    setPixelRange([start], playerPixelRange, bgColor,delay=15,type='fromEnds')

def beerDrink(player):
    beerColor = setRGB(19,8,0)
        # setRGB(236,97,0)
    # 0xec6100

    # p = player + 1
    # if p > numplayers - 1: p = 0

    start1 = getPlayerStartLed(player) + (playerPixelRange // 2)
    start2 = getPlayerStartLed(player)
    start3 = getPlayerStartLed(player) + playerPixelRange

    length = playerPixelRange * 3

    # os.system('mpg123 -q testimages/shotgun-old_school-RA_The_Sun_God-1129942741.mp3 &')

    setPixelRange([start3], length, beerColor, delay=15, type='fromCenter')
    setDelay(1500)
    os.system('mpg123 -q testimages/drinking2.mp3 &')
    setPixelRange([start3], length, bgColor, delay=25, type='fromEnds')
    os.system('mpg123 -q testimages/beer_wood.mp3 &')
    return

def tntEffect():
    r = 236 #getRed(bgColor)     #236
    g = 97 #getGreen(bgColor)   #97
    b = 0 #getBlue(bgColor)    #0

    for x in range(0,numpixels):           # (int x = 8; x < 99; x++)
        flicker = random.randint(0, 8)    #16)             # random(0, 150);
        if flicker == 0:
            r1 = 0
            g1 = 0
            b1 = 0
        else:
            r1 = r // flicker
            g1 = g // flicker
            b1 = b

        if g1 < 0:
            g1 = 0
        if r1 < 0:
            r1 = 0
        if b1 < 0:
            b1 = 0

        strip.setPixelColor(x, r1, g1, b1)

    strip.show()
    setDelay(random.randint(50, 120))

def random1():

    for cicle in range(10):
        brs = numpy.random.rand(numpixels,1)
        print(len(brs))

        for i, br in enumerate(brs):
            r = int(getRed(bgColor) * br)
            g = int(getGreen(bgColor) * br)
            b = int(getBlue(bgColor) * br)
            strip.setPixelColor(i,setRGB(r,g,b))

        strip.show()
        setDelay(500)