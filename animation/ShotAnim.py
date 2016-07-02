import os

from animation.Strip      import Strip
from animation.Animation  import Animation
from animation.AnimThread import AnimThread


class ShotAnim(Animation):
    BLOOD_COLOR = 0xff0000

    # player e.g 1-4
    def __init__(self, player):
        super(ShotAnim, self).__init__(-1)
        self.player = player


    def animate(self):
        print("shot player {0} progress {1}".format(self.player, self.progress))
        if not self.progress:
            os.system('mpg123 -q testimages/shotgun-old_school-RA_The_Sun_God-1129942741.mp3 &')

        #flash
        if 50 < self.progress <= 50 + 20:
            AnimThread.strip.set_brightness(50)

        if 50 + 20 < self.progress <= 50 + 20 + 20:
            AnimThread.strip.set_brightness(255)

        if 50 + 20 + 20 < self.progress <= 50 + 20 + 20 + 100:
            AnimThread.strip.set_brightness(Strip.brightness)

        ##blood
        #start_pos = Strip.numpixels // 4 * (self.player - 1)
        #radius = Strip.numpixels // 8

        #if 50 + 20 + 20 + 100 < self.progress <= 50 + 20 + 20 + 100 + radius * 5 + 400:
        #    cnt = self.progress - (50 + 20 + 20 + 100)
        #    rng = radius * min(1, cnt / 5)
        #    for i in range(rng):
        #        AnimThread.strip.set_color_range(start_pos + radius - i, start_pos + radius + i, self.BLOOD_COLOR)

        #if 50 + 20 + 20 + 100 + radius * 5 + 400 < self.progress <= 50 + 20 + 20 + 100 + radius * 5 + 400 + radius * 90:
        #    cnt = self.progress - (50 + 20 + 20 + 100 + radius * 5 + 400)
        #    for i in range(radius * (1 - cnt // (radius * 5))):
        #        AnimThread.strip.set_color_range(start_pos + radius - i, start_pos + radius + i, self.BLOOD_COLOR)

        #if 50 + 20 + 20 + 100 + radius * 5 + 400 + radius * 90 < self.progress:
        #    self.is_finished = True
