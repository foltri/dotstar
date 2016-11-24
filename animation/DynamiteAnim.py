import os
import random

import subprocess

from animation.Animation import Animation
from animation.Strip import Strip


class DynamiteAnim(Animation):
    # TNT2_MP3_LENGTH = 1000

    def __init__(self, root):
        super(DynamiteAnim, self).__init__(root, duration=-1, priority=1)
        self.next_time = 10


    def animate(self):
        # if self.progress % self.TNT2_MP3_LENGTH == 0:
        #     subprocess.Popen(["mpg123", "-q", "testimages/tnt2.mp3"])

        if self.progress == self.next_time:
            self.randomizeLeds(0,8)
            self.next_time = self.progress + 50 #random.randint(50, 120)

        self.is_frame_to_send = True


    def on_remove(self):
        # TODO: get subprocess ID and kill process with that
        # subprocess.Popen(["pkill", "mpg123"])
        pass

