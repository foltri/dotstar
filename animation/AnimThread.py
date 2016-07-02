from threading import Thread

import time

from animation import Strip


class AnimThread:
    strip = Strip.Strip()

    def __init__(self):
        self.is_running = True
        self.animations = []

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def stop(self):
        self.is_running = False

    def update(self):
        print ("animthread update")
        while self.is_running:
            for anim in self.animations:  # sorted, new entries override buffer
                anim.tick()

            # update physical strip
            self.strip.update()

            # deletes old entries, I hope it remains sorted
            self.animations = [item for item in self.animations if not item.is_finished]

            time.sleep(1 / 30)

    def add(self, anim):
        self.animations.append(anim)
