from __future__ import division

import os

from animation.Animation import Animation
from animation.Strip import Strip


class ShotAnim(Animation):
    def __init__(self, root, player, delay=0):
        super(ShotAnim, self).__init__(root, duration=-1)
        self.color = 0xff0000
        self.player = player
        self.next_time = 0

        self.start_pos = Strip.NUMPIXELS // 4 * (self.player - 1)
        self.radius = Strip.NUMPIXELS // 8
        self.counter = 0
        self.counter1 = self.radius
        self.step = "flash"
        self.next_time = delay
        self.cnt = 0
        self.is_first_run = True


    def animate(self):

        if self.progress >= self.next_time:
            if self.is_first_run:
                # os.system('mpg123 -q testimages/shotgun-old_school-RA_The_Sun_God-1129942741.mp3 &')
                self.is_first_run = False

            if self.step == "flash":
                self.root.STRIP.set_brightness(50)
                self.setDelay(20)
                self.step = "flash1"
            elif self.step == "flash1":
                self.root.STRIP.set_brightness(225)
                self.setDelay(20)
                self.step = "flash2"
            elif self.step == "flash2":
                self.root.STRIP.set_brightness(Strip.BRIGHTNESS)
                self.setDelay(100)
                self.step = "from_center"

            elif self.step == "from_center":
                # kozeprol ki (180ms)
                if self.counter <= self.radius:
                    self.counter += 1
                    self.cnt = self.counter
                    # self.next_time = self.progress + 5
                    self.setDelay(10)
                else:
                    self.step = "from_ends"
                    self.setDelay(400)

            elif self.step == "from_ends":
                # kintrol vissza
                self.counter1 -= 1
                self.cnt = self.counter1
                self.setDelay(90)

                if self.counter1 <= 0:
                    self.is_finished = True


        self.root.STRIP.set_color_range(self.start_pos + self.radius - self.cnt, self.start_pos + self.radius + self.cnt, self.color)
        self.root.STRIP.set_color_range(self.start_pos - 1, self.start_pos + self.radius - self.cnt, Strip.DEFAULT_COLOR)
        self.root.STRIP.set_color_range(self.start_pos + self.radius + self.cnt, self.start_pos + 2 * self.radius + 1, Strip.DEFAULT_COLOR)

        # 2nd strip
        self.root.STRIP.set_color_range2(self.start_pos + self.radius - self.cnt,
                                        self.start_pos + self.radius + self.cnt, self.color)
        self.root.STRIP.set_color_range2(self.start_pos - 1, self.start_pos + self.radius - self.cnt,
                                        Strip.DEFAULT_COLOR)
        self.root.STRIP.set_color_range2(self.start_pos + self.radius + self.cnt, self.start_pos + 2 * self.radius + 1,
                                        Strip.DEFAULT_COLOR)

        self.is_frame_to_send = True
