import os

import atmo_dotstar
import pygame
from pygame.locals import *

LEFT = 1
MIDDLE = 2
RIGHT = 3
SCROLL_UP = 4
SCROLL_DOWN = 5
exit = False

pygame.init()
window = pygame.display.set_mode((100, 100))

atmo_dotstar.strip.begin()  # Initialize pins for output
atmo_dotstar.strip.setBrightness(atmo_dotstar.BRIGHTNESS)

atmo_dotstar.setBackground(atmo_dotstar.bgColor)

while True:

    for event in pygame.event.get(): # nem mukodik, mert alakad a receive-nel!!

        if event.type == MOUSEMOTION:
            pass

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                atmo_dotstar.gunShot(1)
            if event.key == pygame.K_2:
                atmo_dotstar.gunShot(2)
            if event.key == pygame.K_3:
                atmo_dotstar.gunShot(3)
            if event.key == pygame.K_4:
                atmo_dotstar.gunShot(4)

            if event.key == pygame.K_q:
                atmo_dotstar.gGunShot(1)
            if event.key == pygame.K_w:
                atmo_dotstar.gGunShot(2)
            if event.key == pygame.K_e:
                atmo_dotstar.gGunShot(3)
            if event.key == pygame.K_r:
                atmo_dotstar.gGunShot(4)

            if event.key == pygame.K_a:
                atmo_dotstar.arrowShot()

            if event.key == pygame.K_z:
                atmo_dotstar.random()

            if event.key == pygame.K_c:
                atmo_dotstar.beerDrink(3)

        if event.type == pygame.QUIT:
            exit = True
            break

    if exit:
        break
