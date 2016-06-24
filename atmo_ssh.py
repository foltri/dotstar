import os

import atmo_dotstar
import pygame
from pygame.locals import *
import server

exit = False

pygame.init()
window = pygame.display.set_mode((100, 100))

atmo_dotstar.strip.begin()  # Initialize pins for output
atmo_dotstar.strip.setBrightness(atmo_dotstar.BRIGHTNESS)

atmo_dotstar.setBackground(atmo_dotstar.bgColor)

while True:
    m = server.receive()

    if m == 'shot1':
        atmo_dotstar.gunShot(3)
    elif m == 'gatling':
        atmo_dotstar.gGunShot(3)
    # elif message == 'shot2':
    #     atmo_dotstar.gunShot(2)
    # elif message == 'shot3':
    #     atmo_dotstar.gunShot(3)
    # elif message == 'shot4':
    #     atmo_dotstar.gunShot(4)
    elif m == 'arrow':
        atmo_dotstar.arrowShot()
    elif m == 'beer':
        atmo_dotstar.beerDrink(3)

    # elif m == 'tnt_on':
    #     on = True
    #     while on:
    #         if a.read() == 'tnt_off':
    #             on = False
    #         else:
    #             atmo_dotstar.tntEffect()

    elif m == 'exit':
        server.close()
        break


