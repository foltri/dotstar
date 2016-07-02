from animation.Animation import Animation
from animation.AnimThread import AnimThread
from animation.Strip import Strip


class TestAnim(Animation):
    def __init__(self, player):
        super(TestAnim, self).__init__(144)
        self.player = player

    def animate(self):
        if self.progress == 0:
            AnimThread.strip.set_color_range(0, Strip.numpixels, 0xff0000)

        AnimThread.strip.set_color(max(0, self.progress-1), 0xff00ff)
        AnimThread.strip.set_color(self.progress, 0xff00ff)
        print("Fire anim at {} {}".format(self.progress, self.player))
