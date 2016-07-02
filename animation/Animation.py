class Animation(object):
    def __init__(self, dur):
        self.duration = dur
        self.progress = dur
        self.is_finished = False

    def tick(self):
        if self.progress > 0:
            self.animate()
            self.progress -= 1
        else:
            self.is_finished = True

    def is_finished(self):
        return self.is_finished

    # override this to do the animation
    def animate(self):
        pass
