from animation.Animation import Animation
from animation.AnimThread import AnimThread
from animation.Strip import Strip


class TestAnim(Animation):
    def __init__(self, color):
        super(TestAnim, self).__init__(144)
        self.color = color

    def animate(self):
        AnimThread.strip.set_color_range(0, Strip.NUMPIXELS, self.color)
        AnimThread.strip.set_brightness(200)
        print("test anim at {} {}".format(self.progress, self.color))
