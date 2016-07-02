is_emulator = False
try:
    from dotstar import Adafruit_DotStar
except ImportError:
    is_emulator = True
    from DotStar_Emulator import Adafruit_DotStar


class Strip(object):
    brightness = 200
    numpixels = 144  # Number of LEDs in strip
    numplayers = 4
    playerPixelRange = numpixels // numplayers

    # Here's how to control the strip from any two GPIO pins:
    datapin = 23
    clockpin = 24

    def __init__(self):
        self._leds = [0xec6100 for x in range(self.numpixels)]  # colors
        self._brightness = 64

        if not is_emulator:
            self.strip = Adafruit_DotStar(self.numpixels, self.datapin, self.clockpin, order='bgr')
        else:
            self.strip = Adafruit_DotStar(self.numpixels, self.datapin, self.clockpin)  # , order='bgr'
        self.strip.begin()
        self.strip.setBrightness(self._brightness)
        self.strip.show()

    def set_color(self, pos, color):
        self._leds[pos] = color

    def set_color_range(self, start, end, color):
        for i in range(start, end):
            self.set_color(i, color)

    # def set_color(self, pos, r, g, b):
    #     color = r << 16 | g << 8 | b
    #     self.set_color(pos, color)

    def set_brightness(self, brightness):
        self._brightness = brightness

    def update(self):
        for pos, led in enumerate(self._leds):
            self.strip.setPixelColor(pos, led)
        self.strip.setBrightness(self._brightness)
        self.strip.show()
