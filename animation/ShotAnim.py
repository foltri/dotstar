from __future__ import division
from animation.Animation import Animation
from animation.Strip import Strip


class ShotAnim(Animation):
    def __init__(self, root, player):
        super(ShotAnim, self).__init__(root, duration=-1)
        self.color = 0xff0000
        self.player = player
        self.next_time = 0

        self.start_pos = Strip.NUMPIXELS // 4 * (self.player - 1)
        self.radius = Strip.NUMPIXELS // 8
        self.counter = 0
        self.counter1 = self.radius
        self.step = "flash"
        self.next_time = 0
        self.cnt = 0

    def animate(self):

        # os.system('mpg123 -q testimages/shotgun-old_school-RA_The_Sun_God-1129942741.mp3 &')
        # setDelay(50)

        if self.progress >= self.next_time:
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
                    self.setDelay(5)
                else:
                    self.step = "from_ends"
                    self.setDelay(400)

            elif self.step == "from_ends":
                # kintrol vissza
                # if self.progress >= 480:
                if self.next_time == self.progress:
                    self.counter1 -= 1
                    self.cnt = self.counter1
                    self.setDelay(90)

                    if self.counter1 <= 0:
                        self.is_finished = True

        self.root.STRIP.set_color_range(self.start_pos + self.radius - self.cnt, self.start_pos + self.radius + self.cnt, self.color)
        self.root.STRIP.set_color_range(self.start_pos -1, self.start_pos + self.radius - self.cnt, Strip.DEFAULT_COLOR)
        self.root.STRIP.set_color_range(self.start_pos + self.radius + self.cnt, self.start_pos + 2 * self.radius + 1, Strip.DEFAULT_COLOR)
        self.is_frame_to_send = True
