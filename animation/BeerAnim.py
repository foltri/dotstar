from animation.Animation import Animation
from animation.AnimThread_old import AnimThread


class BeerAnim(Animation):
    def __init__(self, player):
        super(BeerAnim, self).__init__(144)
        self.player = player

    def animate(self):
        AnimThread.strip.set_color(self.progress, 0xff00ff)
        print("Fire anim at {} {}".format(self.progress, self.player))
