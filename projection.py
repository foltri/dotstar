import pygame
from pygame.locals import *
import pyganim
import copy

WIDTH, HEIGHT = 1280, 800
BACKGROUND = pygame.Color(0,0,0)

LEFT = 1
MIDDLE = 2
RIGHT = 3
SCROLL_UP = 4
SCROLL_DOWN = 5

radius = 0
mouseX, mouseY = 0, 0
position = (0, 0)
exit = False

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT),pygame.DOUBLEBUF, 32)

fps = pygame.time.Clock()

# create the animation objects   ('filename of image',    duration_in_seconds)
boltAnim = pyganim.PygAnimation([('testimages/bolt_strike_0001.png', 0.1),
                                 ('testimages/bolt_strike_0002.png', 0.1),
                                 ('testimages/bolt_strike_0003.png', 0.1),
                                 ('testimages/bolt_strike_0004.png', 0.1),
                                 ('testimages/bolt_strike_0005.png', 0.1),
                                 ('testimages/bolt_strike_0006.png', 0.1),
                                 ('testimages/bolt_strike_0007.png', 0.1),
                                 ('testimages/bolt_strike_0008.png', 0.1),
                                 ('testimages/bolt_strike_0009.png', 0.1),
                                 ('testimages/bolt_strike_0010.png', 0.1)],loop=False)

fireAnim = pyganim.PygAnimation([('testimages/flame_a_0001.png', 0.1),
                                 ('testimages/flame_a_0002.png', 0.1),
                                 ('testimages/flame_a_0003.png', 0.1),
                                 ('testimages/flame_a_0004.png', 0.1),
                                 ('testimages/flame_a_0005.png', 0.1),
                                 ('testimages/flame_a_0006.png', 0.1)],loop=False)

bombAnim = pyganim.PygAnimation([('testimages/bomb4-13.png', 0.07),
                                 ('testimages/bomb4-14.png', 0.07),
                                 ('testimages/bomb4-15.png', 0.07),
                                 ('testimages/bomb4-16.png', 0.07),
                                 ('testimages/bomb4-17.png', 0.07)], loop=False)


bloodAnim11 = pyganim.PygAnimation([('testimages/blood1-01.png', 0.01),
                                    ('testimages/blood2-01.png', 0.01),
                                    ('testimages/blood3-01.png', 0.01),
                                    ('testimages/blood4-01.png', 1),
                                    ('testimages/blood5-01.png', 0.2),
                                    ('testimages/blood6-01.png', 0.2),
                                    ('testimages/blood7-01.png', 0.2),
                                    ('testimages/blood8-01.png', 0.2),
                                    ('testimages/blood9-01.png', 0.2),
                                    ('testimages/blood10-01.png', 0.2),
                                    ('testimages/blood11-01.png', 0.2),
                                    ('testimages/blood12-01.png', 0.2),
                                    ('testimages/blood13-01.png', 0.2),
                                    ('testimages/blood14-01.png', 0.2),
                                    ('testimages/blood15-01.png', 0.2),
                                    ('testimages/blood16-01.png', 0.2),
                                    ('testimages/blood17-01.png', 0.2),
                                    ('testimages/blood18-01.png', 0.2),
                                    ('testimages/blood19-01.png', 0.2),
                                    ('testimages/blood20-01.png', 0.2),
                                    ('testimages/blood21-01.png', 0.2),
                                    ('testimages/blood22-01.png', 0.2),
                                    ('testimages/blood23-01.png', 0.2)], loop=False)

bloodAnim12 = pyganim.PygAnimation([('testimages/blood1-01.png', 0.01),
                                    ('testimages/blood2-01.png', 0.01),
                                    ('testimages/blood3-01.png', 0.01),
                                    ('testimages/blood4-01.png', 1),
                                    ('testimages/blood5-01.png', 0.2),
                                    ('testimages/blood6-01.png', 0.2),
                                    ('testimages/blood7-01.png', 0.2),
                                    ('testimages/blood8-01.png', 0.2),
                                    ('testimages/blood9-01.png', 0.2),
                                    ('testimages/blood10-01.png', 0.2),
                                    ('testimages/blood11-01.png', 0.2),
                                    ('testimages/blood12-01.png', 0.2),
                                    ('testimages/blood13-01.png', 0.2),
                                    ('testimages/blood14-01.png', 0.2),
                                    ('testimages/blood15-01.png', 0.2),
                                    ('testimages/blood16-01.png', 0.2),
                                    ('testimages/blood17-01.png', 0.2),
                                    ('testimages/blood18-01.png', 0.2),
                                    ('testimages/blood19-01.png', 0.2),
                                    ('testimages/blood20-01.png', 0.2),
                                    ('testimages/blood21-01.png', 0.2),
                                    ('testimages/blood22-01.png', 0.2),
                                    ('testimages/blood23-01.png', 0.2)], loop=False)

bloodAnim13 = pyganim.PygAnimation([('testimages/blood1-01.png', 0.01),
                                    ('testimages/blood2-01.png', 0.01),
                                    ('testimages/blood3-01.png', 0.01),
                                    ('testimages/blood4-01.png', 1),
                                    ('testimages/blood5-01.png', 0.2),
                                    ('testimages/blood6-01.png', 0.2),
                                    ('testimages/blood7-01.png', 0.2),
                                    ('testimages/blood8-01.png', 0.2),
                                    ('testimages/blood9-01.png', 0.2),
                                    ('testimages/blood10-01.png', 0.2),
                                    ('testimages/blood11-01.png', 0.2),
                                    ('testimages/blood12-01.png', 0.2),
                                    ('testimages/blood13-01.png', 0.2),
                                    ('testimages/blood14-01.png', 0.2),
                                    ('testimages/blood15-01.png', 0.2),
                                    ('testimages/blood16-01.png', 0.2),
                                    ('testimages/blood17-01.png', 0.2),
                                    ('testimages/blood18-01.png', 0.2),
                                    ('testimages/blood19-01.png', 0.2),
                                    ('testimages/blood20-01.png', 0.2),
                                    ('testimages/blood21-01.png', 0.2),
                                    ('testimages/blood22-01.png', 0.2),
                                    ('testimages/blood23-01.png', 0.2)], loop=False)

bloodAnim14 = pyganim.PygAnimation([('testimages/blood1-01.png', 0.01),
                                    ('testimages/blood2-01.png', 0.01),
                                    ('testimages/blood3-01.png', 0.01),
                                    ('testimages/blood4-01.png', 1),
                                    ('testimages/blood5-01.png', 0.2),
                                    ('testimages/blood6-01.png', 0.2),
                                    ('testimages/blood7-01.png', 0.2),
                                    ('testimages/blood8-01.png', 0.2),
                                    ('testimages/blood9-01.png', 0.2),
                                    ('testimages/blood10-01.png', 0.2),
                                    ('testimages/blood11-01.png', 0.2),
                                    ('testimages/blood12-01.png', 0.2),
                                    ('testimages/blood13-01.png', 0.2),
                                    ('testimages/blood14-01.png', 0.2),
                                    ('testimages/blood15-01.png', 0.2),
                                    ('testimages/blood16-01.png', 0.2),
                                    ('testimages/blood17-01.png', 0.2),
                                    ('testimages/blood18-01.png', 0.2),
                                    ('testimages/blood19-01.png', 0.2),
                                    ('testimages/blood20-01.png', 0.2),
                                    ('testimages/blood21-01.png', 0.2),
                                    ('testimages/blood22-01.png', 0.2),
                                    ('testimages/blood23-01.png', 0.2)], loop=False)

bloodAnim = pyganim.PygAnimation([('testimages/blood2.1-01.png', 0.01),
                                  ('testimages/blood2.2-01.png', 0.01),
                                  ('testimages/blood2.3-01.png', 0.01),
                                  ('testimages/blood2.4-01.png', 1),
                                  ('testimages/blood2.5-01.png', 0.2),
                                  ('testimages/blood2.6-01.png', 0.2),
                                  ('testimages/blood2.7-01.png', 0.2),
                                  ('testimages/blood2.8-01.png', 0.2),
                                  ('testimages/blood2.9-01.png', 0.2),
                                  ('testimages/blood2.10-01.png', 0.2),
                                  ('testimages/blood2.11-01.png', 0.2),
                                  ('testimages/blood2.12-01.png', 0.2),
                                  ('testimages/blood2.13-01.png', 0.2),
                                  ('testimages/blood2.14-01.png', 0.2),
                                  ('testimages/blood2.15-01.png', 0.2),
                                  ('testimages/blood2.16-01.png', 0.2),
                                  ('testimages/blood2.17-01.png', 0.2),
                                  ('testimages/blood2.18-01.png', 0.2),
                                  ('testimages/blood2.19-01.png', 0.2),
                                  ('testimages/blood2.20-01.png', 0.2),
                                  ('testimages/blood2.21-01.png', 0.2),
                                  ('testimages/blood2.22-01.png', 0.2),
                                  ('testimages/blood2.23-01.png', 0.2)], loop=False)

smokeAnim = pyganim.PygAnimation([('testimages/smoke_puff_0001.png', 0.1),
                                 ('testimages/smoke_puff_0002.png', 0.1),
                                 ('testimages/smoke_puff_0003.png', 0.1),
                                 ('testimages/smoke_puff_0004.png', 0.1),
                                 ('testimages/smoke_puff_0005.png', 0.1),
                                 ('testimages/smoke_puff_0006.png', 0.1),
                                 ('testimages/smoke_puff_0007.png', 0.1),
                                 ('testimages/smoke_puff_0008.png', 0.1),
                                 ('testimages/smoke_puff_0009.png', 0.1),
                                 ('testimages/smoke_puff_0010.png', 0.1)],loop=False)

# bombAnim = copy.copy(bombAnim1)
# bombAnim.rotate(-270)

# bloodAnim11.rotate(-270)

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('testimages/layout2.jpg', [0,0])



def drawResolveZonesOnScreen(zones):
    for zone in zones:
        window.blit(zone.image, zone.rect)

class Animation(pygame.sprite.Sprite):
    def __init__(self, zone, width, height, anim, rotation, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.image = anim
        self.image.scale((width, height))  # set size of animation

        if abs(rotation) > 0:
            self.image.rotate(rotation)

        self.image.convert()


        left = zone.rect.left + (zone.rect.width - width)//2    # set same center as containing zone
        top = zone.rect.top + (zone.rect.height - height)//2
        self.rect = pygame.Rect(pos_x, pos_y, width, height)

    def play(self):
        self.image.play()

    def stop(self):
        self.image.stop()



class ResolveZone(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, width, height, pos_x, pos_y, rotation):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.rotation = rotation

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height],pygame.SRCALPHA, 32)

        self.image.fill(pygame.Color(160, 0, 0, 0))

        pygame.draw.rect(self.image,pygame.Color(150, 150, 150, 1), Rect(0, 0, width, height),0)
        self.image = pygame.transform.rotate(self.image, rotation)

        # self.mask = pygame.mask.from_threshold(self.image, pygame.Color(149,149,149, 0), (151,151,151, 2))
        self.mask = pygame.mask.from_surface(self.image,0)


        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        # self.rect = self.image.get_rect()
        self.rect = self.image.get_bounding_rect()
        self.rect.left = pos_x
        self.rect.top = pos_y

        self.anims = []

    def addAnim(self, anim, width, height, pos_x, pos_y, rotation):
            self.anims.append(Animation(self, width, height, anim, rotation, pos_x, pos_y))



class PlayZone(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(BACKGROUND)
        self.image.set_alpha(0)
        pygame.draw.circle(self.image, pygame.Color(220, 0, 0), (width // 2, height // 2), width // 2, 1)

        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

        self.anims = []

    def addAnims(self, anims):
        for anim in anims:
            self.anims.append(Animation(self, 100, 100, anim, 0, 0, 0))



offset = 250
playZone = PlayZone(300, 300, WIDTH // 2, HEIGHT // 2)
playZone.addAnims([bloodAnim, bombAnim])

resolveZones = []
# resolveZones.append(ResolveZone(150, 150, WIDTH // 2 + offset, HEIGHT // 2))
# resolveZones.append(ResolveZone(150, 150, WIDTH // 2 - offset, HEIGHT // 2))
# resolveZones.append(ResolveZone(150, 150, WIDTH // 2, HEIGHT // 2 - offset))
# resolveZones.append(ResolveZone(150, 150, WIDTH // 2, HEIGHT // 2 + offset))

resolveZones.append(ResolveZone(348, 131, 724, 0, -50))
resolveZones[0].addAnim(bloodAnim11, 308, 233, 597, 58, -146)

resolveZones.append(ResolveZone(348, 131, 742, 433, -125))
resolveZones[1].addAnim(bloodAnim12, 308, 233, 605, 354, -216)


resolveZones.append(ResolveZone(348, 131, 261, 505, -215))
resolveZones[2].addAnim(bloodAnim13, 308, 233, 328, 363, -308)


resolveZones.append(ResolveZone(348, 131, 226, 0, -306))
resolveZones[3].addAnim(bloodAnim14, 308, 233, 289, 63, -36)




# for zone in resolveZones:
#     zone.addAnims([boltAnim, bombAnim, smokeAnim])


while True:

    for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            mouseX, mouseY = event.pos

        # Beer
        if event.type == MOUSEBUTTONDOWN and event.button == RIGHT:
            if playZone.rect.collidepoint(mouseX, mouseY):
                playZone.anims[0].play()

        # Shot
        if event.type == MOUSEBUTTONDOWN and event.button == LEFT:
            for zone in resolveZones:
                flag = 0
                try:
                    flag = zone.mask.get_at((mouseX - zone.rect.left, mouseY - zone.rect.top))
                except IndexError:
                    pass
                if flag:
                    zone.anims[0].play()

        # Gatling
        if event.type == MOUSEBUTTONDOWN and (event.button == SCROLL_DOWN or event.button == SCROLL_UP):
            for zone in resolveZones:
                if zone.rect.collidepoint(mouseX,mouseY):
                    for zone in resolveZones:
                        if not zone.rect.collidepoint(mouseX,mouseY):
                            zone.anims[1].play()

        # TNT
        if event.type == MOUSEBUTTONDOWN and event.button == LEFT:
            if playZone.rect.collidepoint(mouseX,mouseY):
                playZone.anims[1].play()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                pygame.display.set_mode([WIDTH, HEIGHT], pygame.FULLSCREEN)
            if event.key == pygame.K_2:
                pygame.display.set_mode([WIDTH, HEIGHT], pygame)


        if event.type == QUIT:
            exit = True
            break

    if exit: break



    window.blit(playZone.image, playZone.rect)
    drawResolveZonesOnScreen(resolveZones)

    # draw animations on screen
    playZone.anims[0].image.blit(window,playZone.anims[0].rect)
    playZone.anims[1].image.blit(window, playZone.anims[1].rect)
    for zone in resolveZones:
        for anim in zone.anims:
            anim.image.blit(window,anim.rect)


    # window.blit(BackGround.image, BackGround.rect)
    pygame.display.update()
    # window.fill(BACKGROUND)
    window.blit(BackGround.image, BackGround.rect)
    fps.tick(30)
