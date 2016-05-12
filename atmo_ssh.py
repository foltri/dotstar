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
    message = server.receive()
    print(message)
    if message == 'shot1':
        atmo_dotstar.gunShot(1)
    elif message == 'shot2':
        atmo_dotstar.gunShot(2)
    elif message == 'shot3':
        atmo_dotstar.gunShot(3)
    elif message == 'shot4':
        atmo_dotstar.gunShot(4)
    elif message == 'exit':
        server.close()
        break

