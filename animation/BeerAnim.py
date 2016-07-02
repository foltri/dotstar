from animation.Animation import Animation
from animation.AnimThread import AnimThread


class BeerAnim(Animation):
    def __init__(self, player):
        super(BeerAnim, self).__init__(10)
        self.player = player

    def animate(self):
        AnimThread.strip.set_color(1, 0x00ffff)
        print("Fire anim at {} {}".format(self.progress, self.player))
        pass
