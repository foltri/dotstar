IS_EMULATOR = False

try:
    from dotstar import Adafruit_DotStar
except ImportError:
    IS_EMULATOR = True
    from DotStar_Emulator import Adafruit_DotStar


# ------------------------------------------------------------------------------#
class Strip(object):
    DEFAULT_COLOR = 0xec6100
    BRIGHTNESS = 120
    # BRIGHTNESS = 60
    NUMPIXELS = 144  # Number of LEDs in strip
    ALLPIXELS = 288
    NUMPLAYERS = 4
    PLAYER_PIXEL_RANGE = NUMPIXELS // NUMPLAYERS

    # Here's how to control the strip from any two GPIO pins:
    # _DATAPIN = 23
    # _CLOCKPIN = 24

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __init__(self):
        self._brightness = self.BRIGHTNESS

        if IS_EMULATOR:
            self.strip = Adafruit_DotStar(self.ALLPIXELS,
                                          self._DATAPIN,
                                          self._CLOCKPIN)
        else:
            self.strip = Adafruit_DotStar(self.ALLPIXELS,order='bgr')  # Use SPI (pins 10=MOSI, 11=SCLK)
            # self.strip = Adafruit_DotStar(self.ALLPIXELS,
            #                               self._DATAPIN,
            #                               self._CLOCKPIN,
            #                               order='bgr')#g

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
    def set_color_range(self, start, end, r, g=None, b=None):
        for i in range(start, end):

            if i > (Strip.NUMPIXELS):
                i -= (Strip.NUMPIXELS)
            elif i < 0:
                i += (Strip.NUMPIXELS)

            if (g is not None and
                        b is not None):
                self.strip.setPixelColor(i, r, g, b)
            else:
                self.strip.setPixelColor(i, r)

    def set_color_range2(self, start, end, r, g=None, b=None):
        for i in range(start + 144, end + 144):

            if i > (Strip.NUMPIXELS + 144):
                i -= (Strip.NUMPIXELS)
            elif i < 144:
                i += (Strip.NUMPIXELS + 144)

            if (g is not None and
                        b is not None):
                self.strip.setPixelColor(i, r, g, b)
            else:
                self.strip.setPixelColor(i, r)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def set_brightness(self, brightness):
        self.strip.setBrightness(brightness)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def show(self):
        self.strip.show()

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def getPlayerStartLed(self, player):
        return self.PLAYER_PIXEL_RANGE * (player - 1)
