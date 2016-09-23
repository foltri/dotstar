import os
import random

import subprocess

from animation.Animation import Animation
from animation.Strip import Strip


class DynamiteAnim(Animation):
    TNT2_MP3_LENGTH = 1000

    def __init__(self, root):
        super(DynamiteAnim, self).__init__(root, duration=-1, priority=1)
        self.next_time = 10
        self.colors = []


    def animate(self):
        if self.progress % self.TNT2_MP3_LENGTH == 0:
            subprocess.Popen(["mpg123", "-q", "testimages/tnt2.mp3"])

        r = 236  # getRed(bgColor)     #236
        g = 97  # getGreen(bgColor)   #97
        b = 0  # getBlue(bgColor)    #0

        self.colors = []
        # print("progress: {}, next: {}".format(self.progress,self.next_time))
        if self.progress == self.next_time:
            for i in range(0, Strip.NUMPIXELS):
                flicker = random.randint(0, 8)  # 16)  # random(0, 150);
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

                self.colors.append((r1,g1,b1))

            self.next_time = self.progress + 30 #random.randint(50, 120)


        for i, color in enumerate(self.colors):
            self.root.STRIP.set_color(i, color[0], color[1], color[2])

        self.is_frame_to_send = True


    def on_remove(self):
        # TODO: get subprocess ID and kill process with that
        subprocess.Popen(["pkill", "mpg123"])

