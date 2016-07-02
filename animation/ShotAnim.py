import os

import subprocess

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

        start_pos = Strip.NUMPIXELS // 4 * (self.player - 1)
        radius = Strip.NUMPIXELS // 8

        if not self.progress:
            # subprocess.call(["mpg123", "-q", "testimages/shotgun-old_school-RA_The_Sun_God-1129942741.mp3"])
            AnimThread.strip.set_color_range(start_pos, start_pos + 2*radius, Strip.DEFAULT_COLOR)

        #flash
        # if 50 < self.progress <= 50 + 20:
        #     AnimThread.strip.set_brightness(50)
        #
        # if 50 + 20 < self.progress <= 50 + 20 + 20:
        #     AnimThread.strip.set_brightness(255)
        #
        # if 50 + 20 + 20 < self.progress <= 50 + 20 + 20 + 100:
        #     AnimThread.strip.set_brightness(Strip.BRIGHTNESS)

        ##blood

        if 50 + 20 + 20 + 100 < self.progress :
            cnt = self.progress - (50 + 20 + 20 + 100)
            AnimThread.strip.set_color_range(start_pos, start_pos + cnt, self.BLOOD_COLOR)
        #
        # if 50 + 20 + 20 + 100 < self.progress <= 50 + 20 + 20 + 100 + radius * 5 + 400:
        #     cnt = self.progress - (50 + 20 + 20 + 100)
        #     rng = radius * min(1, cnt / 5)
        #     AnimThread.strip.set_color_range(start_pos + radius - i, start_pos + radius + i, self.BLOOD_COLOR)

        # if 50 + 20 + 20 + 100 + radius * 5 + 400 < self.progress <= 50 + 20 + 20 + 100 + radius * 5 + 400 + radius * 90:
        #     cnt = self.progress - (50 + 20 + 20 + 100 + radius * 5 + 400)
        #     for i in range(radius * (1 - cnt // (radius * 5))):
        #         AnimThread.strip.set_color_range(start_pos + radius - i, start_pos + radius + i, 0x0000ff)

        if 50 + 20 + 20 + 100 + radius * 5 + 400 + radius * 90 < self.progress:
            self.is_finished = True
