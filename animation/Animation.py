
#------------------------------------------------------------------------------#
import random


class Animation(object):

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    @property
    def is_finished(self):
        return self._is_finished

    @is_finished.setter
    def is_finished(self, value):
        self._is_finished = value


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __init__(self, root, duration, priority=2):
        self.root             = root
        self.duration         = duration
        self.progress         = 0
        self.is_finished      = False
        self.is_frame_to_send = False
        self.priority         = priority
        self.next_time = 0


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def tick(self):
        if (self.duration == -1 or
            self.progress < self.duration):
                self.animate()
                self.progress += 2
        else:
            self.is_finished = True


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    # override this to do the animation
    def animate(self):
        pass

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def on_remove(self):
        pass

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    # delay must be divisible by 1
    def setDelay(self, delay):
        self.next_time = self.progress + delay

    def randomizeLeds(self, min_divider, max_divider, current_color=(236,97,0), strip1=True, strip2=True):

        for i in range(0, self.root.STRIP.NUMPIXELS):
            flicker = random.randint(min_divider, max_divider)
            if flicker == 0:
                r1 = 0
                g1 = 0
                b1 = 0
            else:
                r1 = current_color[0] // flicker
                g1 = current_color[1] // flicker
                b1 = current_color[2]

            if g1 < 0:
                g1 = 0
            if r1 < 0:
                r1 = 0
            if b1 < 0:
                b1 = 0

            if strip1:
                self.root.STRIP.set_color(i, r1, g1, b1)
            if strip2:
                self.root.STRIP.set_color2(i, r1, g1, b1)