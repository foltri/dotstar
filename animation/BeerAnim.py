from __future__ import division
from animation.Animation import Animation
from animation.Strip import Strip


class BeerAnim(Animation):
    def __init__(self, root, player):
        super(BeerAnim, self).__init__(root, duration=-1)
        self.color = [19, 8, 0]
        self.player = player
        self.next_time = 0

        self.start_pos = Strip.NUMPIXELS // 4 * (self.player - 1) + Strip.PLAYER_PIXEL_RANGE
        # self.radius = Strip.NUMPIXELS // 8
        self.radius = Strip.PLAYER_PIXEL_RANGE * 3 // 2
        self.counter = 0
        self.counter1 = self.radius
        self.step = "from_center"
        self.next_time = 0
        self.cnt = 0

    def animate(self):
        if self.progress >= self.next_time:
            if self.step == "from_center":
                # kozeprol ki
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
                self.counter1 -= 1
                self.cnt = self.counter1
                self.setDelay(5)

                if self.counter1 <= 0:
                    self.is_finished = True

        # strip bottom
        self.root.STRIP.set_color_range(self.start_pos + self.radius - self.cnt, self.start_pos + self.radius + self.cnt, self.color[0], self.color[1], self.color[2])
        self.root.STRIP.set_color_range(self.start_pos - 1, self.start_pos + self.radius - self.cnt, Strip.DEFAULT_COLOR)
        self.root.STRIP.set_color_range(self.start_pos + self.radius + self.cnt, self.start_pos + 2 * self.radius + 1, Strip.DEFAULT_COLOR)

        # strip top
        self.root.STRIP.set_color_range2(self.start_pos + self.radius - self.cnt,
                                        self.start_pos + self.radius + self.cnt, self.color[0], self.color[1],
                                        self.color[2])
        self.root.STRIP.set_color_range2(self.start_pos - 1, self.start_pos + self.radius - self.cnt,
                                        Strip.DEFAULT_COLOR)
        self.root.STRIP.set_color_range2(self.start_pos + self.radius + self.cnt, self.start_pos + 2 * self.radius + 1,
                                        Strip.DEFAULT_COLOR)

        self.is_frame_to_send = True
