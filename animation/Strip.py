IS_EMULATOR   = False
DEFAULT_COLOR = 0xec6100


try:
    from dotstar import Adafruit_DotStar
except ImportError:
    IS_EMULATOR = True
    from DotStar_Emulator import Adafruit_DotStar

#------------------------------------------------------------------------------#
class Strip(object):
    BRIGHTNESS         = 200
    NUMPIXELS          = 144  # Number of LEDs in strip
    NUMPLAYERS         = 4
    PLAYER_PIXEL_RANGE = NUMPIXELS // NUMPLAYERS

    # Here's how to control the strip from any two GPIO pins:
    _DATAPIN  = 23
    _CLOCKPIN = 24

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __init__(self):
        self._leds = [DEFAULT_COLOR for x in range(self.NUMPIXELS)]  # colors
        self._brightness = 64

        if IS_EMULATOR:
            self.strip = Adafruit_DotStar(self.NUMPIXELS,
                                          self._DATAPIN,
                                          self._CLOCKPIN)
        else:
            self.strip = Adafruit_DotStar(self.NUMPIXELS,
                                          self._DATAPIN,
                                          self._CLOCKPIN,
                                          order='bgr')

        self.strip.begin()
        self.strip.setBrightness(self._brightness)
        self.strip.show()


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def set_color(self, pos, color):
        self._leds[pos] = color


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def set_color_range(self, start, end, color):
        for i in range(start, end):
            self.set_color(i, color)

    # def set_color(self, pos, r, g, b):
    #     color = r << 16 | g << 8 | b
    #     self.set_color(pos, color)


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def set_brightness(self, brightness):
        self._brightness = brightness


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def update(self):
        for pos, led in enumerate(self._leds):
            self.strip.setPixelColor(pos, led)
        self.strip.setBrightness(self._brightness)
        self.strip.show()
