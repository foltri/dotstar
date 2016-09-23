from __future__ import division

import os

from animation.Animation import Animation
from animation.Strip import Strip


class ArrowAnim(Animation):
    def __init__(self, root, player):
        super(ArrowAnim, self).__init__(root, duration=-1)
        self.color = 0xd628da
        self.player = player
        self.next_time = 0

        self.start_pos = Strip.NUMPIXELS // 4 * (self.player - 1)
        self.radius = Strip.NUMPIXELS // 8
        self.counter = 0
        self.counter1 = self.radius
        self.step = "from_center"
        self.cnt = 0
        self.is_first_run = True

    def animate(self):

        if self.is_first_run:
            os.system('mpg123 -q testimages/indian_scream2.mp3 &')
            self.is_first_run = False


        if self.progress >= self.next_time:
            if self.step == "from_center":
                # kozeprol ki (180ms)
                if self.counter <= self.radius:
                    self.counter += 1
                    self.cnt = self.counter
                    self.setDelay(15)
                else:
                    self.step = "from_ends"
                    self.setDelay(700)

            elif self.step == "from_ends":
                self.counter1 -= 1
                self.cnt = self.counter1
                self.setDelay(15)

                if self.counter1 <= 0:
                    self.is_finished = True

        p14 = self.start_pos + self.radius - self.cnt + 18
        p25 = self.start_pos + self.radius + self.cnt + 18
        p3 = self.start_pos - 1 + 18
        p6 = self.start_pos + 2 * self.radius + 1 + 18

        self.root.STRIP.set_color_range(p14, p25, self.color)
        self.root.STRIP.set_color_range(p3, p14, Strip.DEFAULT_COLOR)
        self.root.STRIP.set_color_range(p25, p6, Strip.DEFAULT_COLOR)

        self.is_frame_to_send = True
