from threading import Thread
from Queue import Queue, Empty, PriorityQueue
import time

from animation.Strip import Strip


class AnimThread:
    strip = Strip()
    is_frames_to_send = False # set to send frames to strip

    def __init__(self):
        self.is_running = True
        self.animations = PriorityQueue(0)
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
                    is_frames_to_send = True
                    self.is_bg_set = True
            else:
                self.is_bg_set = False
                print(self.animations.qsize())

            new_animations = PriorityQueue(0) # micsudi ez?
            while True:
                try:
                    anim = self.animations.get(block=False)

                    if not anim.is_finished: # kiszedi a finishelt animokat
                        anim.tick()
                        is_frames_to_send = anim.is_frame_to_send
                        new_animations.put(anim, anim.priority)
                except Empty:
                    break
            self.animations = new_animations

            if is_frames_to_send:   # send to strip
                AnimThread.strip.strip.show()
                is_frames_to_send = False

            time.sleep(20 / 1000)

    def add(self, anim):
        self.animations.put(anim, anim.priority)

    def remove(self, param):
        new_animations = PriorityQueue(0)
        while not self.animations.empty():
            anim = self.animations.get()
            if not isinstance(anim, param):
                new_animations.put(anim, anim.priority)
            else:
                anim.on_remove()

        self.animations = new_animations
