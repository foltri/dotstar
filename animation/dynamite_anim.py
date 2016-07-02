import os
import random

import subprocess

from animation.AnimThread import AnimThread
from animation.Animation import Animation
from animation.Strip import Strip


class DynamiteAnim(Animation):
    def __init__(self):
        super(DynamiteAnim, self).__init__(-1)
        self.next_time = random.randint(50, 120)

    def animate(self):
        if self.progress % 4100 == 0:
            # subprocess.call(["mpg123", "-q", "testimages/tnt2.mp3"])
            pass
        r = 236  # getRed(bgColor)     #236
        g = 97  # getGreen(bgColor)   #97
        b = 0  # getBlue(bgColor)    #0

        if self.progress == self.next_time:
            for x in range(0, Strip.NUMPIXELS):  # (int x = 8; x < 99; x++)
                flicker = random.randint(0, 8)  # 16)             # random(0, 150);
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

                AnimThread.strip.set_color(x, r1, g1, b1)

            AnimThread.strip.strip.show()
            self.next_time = self.progress + random.randint(50, 120)

    def on_remove(self):
        os.system('pkill mpg123')
