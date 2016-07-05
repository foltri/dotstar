import collections
from threading import Thread
from Queue import Queue, Empty, PriorityQueue
import time

from animation.ShotAnim import ShotAnim
from animation.Strip import Strip
from animation.TestAnim import TestAnim
from animation.dynamite_anim import DynamiteAnim

class AnimThread:

    STRIP = Strip()

    def __init__(self, message_pool):
        self.is_running    = True
        self.is_bg_set     = False
        self._message_pool = message_pool
        self.ANIMS = {
            'shot1': lambda: ShotAnim(self, 1),
            'shot2': lambda: ShotAnim(self, 2),
            'shot3': lambda: ShotAnim(self, 3),
            'shot4': lambda: ShotAnim(self, 4),
            'test' : lambda : TestAnim(self)
        }

    def start(self):
        Thread(target=self.update, args=()).start()

    def stop(self):
        self.is_running = False

    def update(self):
        local_data = collections.OrderedDict([('tnt', None)])
        while self.is_running:
            is_frames_to_send = False
            is_any_anim = False

            while True:

                # van uj command?
                try:
                    command = self._message_pool.get(timeout=0.01)
                    print command
                    if command == "tnt_on":
                        local_data["tnt"] = DynamiteAnim(self)
                    elif command == "tnt_off":
                        local_data["tnt"].is_finished = True
                    else:
                        local_data[command] = self.ANIMS[command]()
                except Empty:
                    break

            for command, anim in local_data.items():
                try:
                    if not anim.is_finished:
                        anim.tick()
                        is_frames_to_send = is_frames_to_send or anim.is_frame_to_send
                        is_any_anim = True
                    else:
                        local_data[command] = None
                except AttributeError:
                    pass

            if is_any_anim:
                self.is_bg_set = False
                if is_frames_to_send:
                    self.STRIP.show()

            elif not self.is_bg_set:
                self.STRIP.set_color_range(0, Strip.NUMPIXELS, Strip.DEFAULT_COLOR)
                self.is_bg_set = True
                self.STRIP.show()

            time.sleep(0.01)

