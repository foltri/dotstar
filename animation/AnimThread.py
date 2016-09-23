import collections
import subprocess
import Queue
import time
import Timer

from animation.ArrowAnim import ArrowAnim
from animation.BeerAnim import BeerAnim
from animation.ShotAnim import ShotAnim
from animation.Strip import Strip
from animation.TestAnim import TestAnim
from animation.DynamiteAnim import DynamiteAnim


class AnimThread:

    STRIP = Strip()

    def __init__(self, message_pool):
        self.is_running    = True
        self.is_bg_set     = False
        self._message_pool = message_pool
        self.is_frames_to_send = False
        self.is_any_anim = False
        self.local_data = collections.OrderedDict([('tnt', None)])
        self.ANIMS = {
            'shot1': lambda: ShotAnim(self, 1),
            'shot2': lambda: ShotAnim(self, 2),
            'shot3': lambda: ShotAnim(self, 3),
            'shot4': lambda: ShotAnim(self, 4),
            'arrow1': lambda: ArrowAnim(self, 1),
            'arrow2': lambda: ArrowAnim(self, 2),
            'arrow3': lambda: ArrowAnim(self, 3),
            'arrow4': lambda: ArrowAnim(self, 4),
            'beer1': lambda: BeerAnim(self, 1),
            'beer2': lambda: BeerAnim(self, 2),
            'beer3': lambda: BeerAnim(self, 3),
            'beer4': lambda: BeerAnim(self, 4),
            'test' : lambda : TestAnim(self)
        }

    def start(self):
        # Thread(target=self.update, args=()).start()
        # Timer.Timer(0.001, self.update).run()
        self.update()

    def stop(self):
        self.is_running = False

    def update(self):
        while True:
            t = time.time()
            while True:
                try:
                    command = self._message_pool.get(block=False)
                    print command
                    if command == "tnt_on":
                        if self.local_data["tnt"] is None:
                            self.local_data["tnt"] = DynamiteAnim(self)

                    elif command == "tnt_off":
                        if self.local_data["tnt"] is not None:
                            self.local_data["tnt"].is_finished = True
                            subprocess.Popen(["pkill", "mpg123"])

                    elif command[:7] == "gatling":
                        d = 0
                        player = command[-1]
                        for p in range(1,5):
                            if not p == int(player):
                                self.local_data["{}{}".format(command[:7], str(p))] = ShotAnim(self, p, delay=d)
                                d += 200
                    else:
                        self.local_data[command] = self.ANIMS[command]()
                except Queue.Empty:
                    break

            for command, anim in self.local_data.items():
                try:
                    if not anim.is_finished:
                        anim.tick()
                        self.is_frames_to_send = self.is_frames_to_send or anim.is_frame_to_send
                        self.is_any_anim = True
                    else:
                        self.local_data[command] = None
                except AttributeError:
                    pass

            if self.is_any_anim:
                self.is_bg_set = False
                if self.is_frames_to_send:
                    self.STRIP.show()

            elif not self.is_bg_set:
                self.STRIP.set_color_range(0, Strip.NUMPIXELS, Strip.DEFAULT_COLOR)
                self.STRIP.set_color_range2(0, Strip.NUMPIXELS, Strip.DEFAULT_COLOR)
                self.is_bg_set = True
                self.STRIP.show()

            # 1ms
            next = 0.002 - (time.time() - t)
            if next > 0:
                time.sleep(next)
            else: print(next, len(self.local_data))



