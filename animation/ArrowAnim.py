from __future__ import division
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

    def animate(self):

        # indianColor = 0xd628da
        #
        # start = playerPixelRange * player + playerPixelRange // 2
        #
        # os.system('mpg123 -q testimages/indian_scream2.mp3 &')
        # setPixelRange([start], playerPixelRange, indianColor, delay=15, type='fromCenter')
        # setDelay(1500)
        #
        # setPixelRange([start], playerPixelRange, bgColor, delay=15, type='fromEnds')


        if self.progress >= self.next_time:
            if self.step == "from_center":
                # kozeprol ki (180ms)
                if self.counter <= self.radius:
                    self.counter += 1
                    self.cnt = self.counter
                    # self.next_time = self.progress + 5
                    self.setDelay(15)
                else:
                    self.step = "from_ends"
                    self.setDelay(1500)

            elif self.step == "from_ends":
                # kintrol vissza
                # if self.progress >= 480:
                self.counter1 -= 1
                self.cnt = self.counter1
                self.setDelay(15)

                if self.counter1 <= 0:
                    self.is_finished = True

        self.root.STRIP.set_color_range(self.start_pos + self.radius - self.cnt, self.start_pos + self.radius + self.cnt, self.color)
        self.root.STRIP.set_color_range(self.start_pos -1, self.start_pos + self.radius - self.cnt, Strip.DEFAULT_COLOR)
        self.root.STRIP.set_color_range(self.start_pos + self.radius + self.cnt, self.start_pos + 2 * self.radius + 1, Strip.DEFAULT_COLOR)
        self.is_frame_to_send = True
