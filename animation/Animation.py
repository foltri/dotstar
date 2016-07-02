
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
    def __init__(self, duration):
        self.duration    = duration
        self.progress    = 0
        self.is_finished = False


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def tick(self):
        if self.duration == -1 or self.progress < self.duration:
            self.animate()
            self.progress += 1
        else:
            self.is_finished = True


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    # override this to do the animation
    def animate(self):
        pass

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def on_remove(self):
        pass
