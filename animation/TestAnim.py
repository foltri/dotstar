from __future__ import division
from animation.Animation import Animation
from animation.Strip import Strip


class TestAnim(Animation):
    def __init__(self, root):
        super(TestAnim, self).__init__(root, duration=4000)
        self.color = 0xff0000
        self.player = 2
        self.counter = 0
        self.next_time = 10

    def animate(self):

        start_pos = Strip.NUMPIXELS // 4 * (self.player - 1)
        radius = Strip.NUMPIXELS // 8

        if self.progress == self.next_time:
            self.counter += 1
            self.root.STRIP.set_color_range(start_pos + radius - self.counter, start_pos + radius + self.counter, self.color)
            self.next_time = self.progress + 500
            self.is_frame_to_send = True
        else:
            self.is_frame_to_send = False



# from animation.Animation import Animation
# from animation.AnimThread import AnimThread
# from animation.Strip import Strip
#
#
# class TestAnim(Animation):
#     def __init__(self, color, player):
#         super(TestAnim, self).__init__(800)
#         self.color = color
#         self.player = player
#
#     def animate(self):
#
#         start_pos = Strip.NUMPIXELS // 4 * (self.player - 1)
#         radius = Strip.NUMPIXELS // 8
#
#         if self.progress < 144:
#             cnt = self.progress // 8
#             AnimThread.strip.set_color_range(start_pos + radius - cnt, start_pos + radius + cnt, self.color)
#             self.is_frame_to_send = True
#             return
#         elif self.progress < 544:
#
#             AnimThread.strip.set_color_range(start_pos, start_pos + 2 * radius, self.color)
#             self.is_frame_to_send = True
#             return
#         elif self.progress < 688:
#             cnt = radius - (self.progress - 544) // 4
#             AnimThread.strip.set_color_range(start_pos + radius - cnt, start_pos + radius + cnt, self.color)
#             self.is_frame_to_send = True
#             return
#         else:
#             AnimThread.strip.set_color_range(0, Strip.PLAYER_PIXEL_RANGE, 0xff0000)
#             AnimThread.strip.set_color_range(Strip.PLAYER_PIXEL_RANGE, 2 * Strip.PLAYER_PIXEL_RANGE, 0x00ff00)
#             AnimThread.strip.set_color_range(2 * Strip.PLAYER_PIXEL_RANGE, 3 * Strip.PLAYER_PIXEL_RANGE, 0x0000ff)
#             AnimThread.strip.set_color_range(3 * Strip.PLAYER_PIXEL_RANGE, 4 * Strip.PLAYER_PIXEL_RANGE, 0xff00ff)
#             self.is_frame_to_send = True
#
#             return