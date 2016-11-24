from __future__ import division
from animation.Animation import Animation
from animation.Strip import Strip
import random


class ExplosionAnim(Animation):
    def __init__(self, root):
        super(ExplosionAnim, self).__init__(root, duration=-1)
        self.color = [236, 97, 0]
        self.next_time = 0

        self.radius = Strip.PLAYER_PIXEL_RANGE * 3 // 2
        self.counter = 0
        self.step = "fade_out"
        self.next_time = 0
        self.brightness = 120

    def animate(self):
        if self.progress >= self.next_time:
            if self.step == "fade_out":
                # -20% brightness
                self.color[0] -= self.color[0] * 0.2
                self.color[1] -= self.color[1] * 0.2
                self.root.STRIP.set_color_range(0, Strip.NUMPIXELS, int(self.color[0]), int(self.color[1]), self.color[2])
                self.root.STRIP.set_color_range2(0, Strip.NUMPIXELS, int(self.color[0]), int(self.color[1]), self.color[2])
                self.setDelay(25)
                self.counter += 1
                if self.counter == 10:
                    self.step = "red_in"

            if self.step == "red_in":
                self.color[0] += self.color[0] * 0.1
                self.color[1] += self.color[1] * 0.02
                if self.brightness < 250:
                    self.brightness += 10
                    self.root.STRIP.set_brightness(self.brightness)
                if self.color[0] >= 250:
                    self.color = [int(self.color[0] - self.color[0] * 0.1), int(self.color[1] - self.color[1] * 0.02),0]
                    self.step = "brr"
                else:
                    self.randomizeLeds(1,8,current_color=(int(self.color[0]), int(self.color[1]), self.color[2]))
                    self.setDelay(20)

            if self.step == "brr":
                self.randomizeLeds(1,4,current_color=(self.color[0], self.color[1], self.color[2]))
                self.setDelay(20)
                self.counter += 1
                if self.counter >= 50:
                    self.step = "normalize"

            if self.step == "normalize":
                self.setDelay(20)
                self.color[1] += self.color[1] * 0.02
                self.brightness -= 5
                if self.brightness >= 120:
                    self.root.STRIP.set_brightness(self.brightness)

                if self.color[1] <= 97:
                    self.randomizeLeds(1, 2, current_color=(int(self.color[0]), int(self.color[1]), self.color[2]))
                else:
                    self.step = "end"

            if self.step == "end":
                self.is_finished = True

        self.is_frame_to_send = True
