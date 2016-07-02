try:
    from dotstar import Adafruit_DotStar
except ImportError:
    from DotStar_Emulator import Adafruit_DotStar


class Strip():
    numpixels = 144  # Number of LEDs in strip
    numplayers = 4
    playerPixelRange = numpixels // numplayers

    # Here's how to control the strip from any two GPIO pins:
    datapin = 23
    clockpin = 24

    def __init__(self):
        self._leds = [0x00ff00 for x in range(self.numpixels)]  # colors
        self._brightness = 100

        self.strip = Adafruit_DotStar(self.numpixels, self.datapin, self.clockpin)  # , order='bgr'

    def set_color(self, pos, color):
        self._leds[pos] = color

    def set_color_(self, pos, color):
        self._leds[pos] = color

    def set_brightness(self, brightness):
        self._brightness = brightness

    def update(self):
        for pos, led in enumerate(self._leds):
            self.strip.setPixelColor(pos, led)
        self.strip.setBrightness(self._brightness)
        self.strip.show()
