from threading import Thread
from Queue import Queue
import time

from animation.Strip import Strip


class AnimThread:
    strip = Strip()

    def __init__(self):
        self.is_running = True
        self.animations = Queue()

    def start(self):
        Thread(target=self.update, args=()).start()

    def stop(self):
        self.is_running = False

    def update(self):
        while self.is_running:

            # default bg
            AnimThread.strip.set_color_range(0, Strip.NUMPIXELS, Strip.DEFAULT_COLOR)
            if self.animations.empty():
                AnimThread.strip.strip.show()
            else:
                print(self.animations.qsize())

            new_animations = Queue()
            while not self.animations.empty():
                anim = self.animations.get()

                if not anim.is_finished:
                    anim.tick()
                    new_animations.put(anim)

            self.animations = new_animations

            time.sleep(20 / 1000)

    def add(self, anim):
        self.animations.put(anim)

    def remove(self, param):
        new_animations = Queue()
        while not self.animations.empty():
            anim = self.animations.get()
            if not isinstance(anim, param):
                new_animations.put(anim)

        self.animations = new_animations
