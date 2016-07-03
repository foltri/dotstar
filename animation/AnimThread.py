from threading import Thread
from Queue import Queue, Empty
import time

from animation.Strip import Strip


class AnimThread:
    strip = Strip()

    def __init__(self):
        self.is_running = True
        self.animations = Queue()
        self.is_bg_set = False

    def start(self):
        Thread(target=self.update, args=()).start()

    def stop(self):
        self.is_running = False

    def update(self):
        while self.is_running:

            if self.animations.empty():
                if not self.is_bg_set:
                    # default bg
                    AnimThread.strip.set_color_range(0, Strip.NUMPIXELS, Strip.DEFAULT_COLOR)
                    AnimThread.strip.strip.show() # todo flag kene ide is es egy helyen kuldeni
                    self.is_bg_set = True
            else:
                self.is_bg_set = False
                print(self.animations.qsize())

            new_animations = Queue() # micsudi ez?
            while True:
                try:
                    anim = self.animations.get(block=False)

                    if not anim.is_finished: # kiszedi a finishelt animokat
                        anim.tick()
                        new_animations.put(anim)
                except Empty:
                    break
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
            else:
                anim.on_remove()

        self.animations = new_animations
