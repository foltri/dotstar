
#------------------------------------------------------------------------------#
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
                self.progress += 10
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
    # delay must be divisible by 5
    def setDelay(self, delay):
        self.next_time = self.progress + delay
