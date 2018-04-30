import time
from neopixel import *

class LEDcontroller:
	_LED_COUNT=25		#adapt LEDcount (first number) to real value

	def __init__(self):
		print('Constructing LED library')
		self.strip = Adafruit_NeoPixel(self._LED_COUNT, 10, 800000, 10, False, 255, 0)
		print('Initializing LED library')
		self.strip.begin()
		print('LED controller initialized')

	def run(self):
		for i in range(0, self._LED_COUNT-1):
			self.strip.setPixelColorRGB(i, 255, 0, 100)
		self.strip.show()

	def update(self):
		pass

	def shutdown(self):
		for i in range(0, self._LED_COUNT-1):
			self.strip.setPixelColorRGB(i, 0, 0, 0)
		self.strip.show()
		time.sleep(.5)
