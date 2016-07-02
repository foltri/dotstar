IS_EMULATOR = False

try:
    from dotstar import Adafruit_DotStar
except ImportError:
    IS_EMULATOR = True
    from DotStar_Emulator import Adafruit_DotStar


# ------------------------------------------------------------------------------#
class Strip(object):
    DEFAULT_COLOR = 0xec6100
    BRIGHTNESS = 200
    NUMPIXELS = 144  # Number of LEDs in strip
    NUMPLAYERS = 4
    PLAYER_PIXEL_RANGE = NUMPIXELS // NUMPLAYERS

    # Here's how to control the strip from any two GPIO pins:
    _DATAPIN = 23
    _CLOCKPIN = 24

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __init__(self):
        self._brightness = 64

        if IS_EMULATOR:
            self.strip = Adafruit_DotStar(self.NUMPIXELS,
                                          self._DATAPIN,
                                          self._CLOCKPIN)
        else:
            self.strip = Adafruit_DotStar(self.NUMPIXELS,
                                          self._DATAPIN,
                                          self._CLOCKPIN,
                                          order='bgr')#g

        self.strip.begin()
        self.strip.setBrightness(self._brightness)
        self.strip.show()

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def set_color(self, pos, r, g=None, b=None):
        if (g is not None and
                    b is not None):
            self.strip.setPixelColor(pos, r, g, b)
        else:
            self.strip.setPixelColor(pos, r)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def set_color_range(self, start, end, color):
        for i in range(start, end):
            self.strip.setPixelColor(i, color)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def set_brightness(self, brightness):
        self.strip.setBrightness(brightness)
        self.strip.show()

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def show(self):
        self.strip.show()
