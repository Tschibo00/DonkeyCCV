import time
import math
import random
from neopixel import *

strip=None			#global singleton for strip driver

class LEDcontroller:
	_LED_COUNT=7		#total lED count
	_LED_TAIL=0
	_LED_MANE=1		#3 consecutive LEDs
	_LED_HORN=4
	_LED_EYES=5		#2 consecutive LEDs
	flicker=False
	mane_delay=10

	def __init__(self):
		global strip
		print('Initializing LEDs')
		strip = Adafruit_NeoPixel(self._LED_COUNT, 10, 1200000, 10, False, 255, 0)
		strip.begin()

	def run(self):
		global strip
		#let tail flicker in red/pink colors
		self.flicker=not self.flicker
		if self.flicker:
			strip.setPixelColorRGB(self._LED_TAIL,0,255,int(math.sin(time.time()*2.)*50.+50.))
		else:
			strip.setPixelColorRGB(self._LED_TAIL,0,0,0)
		#let mane glow red/pink with random white flashes
		self.mane_delay-=1
		if self.mane_delay==0:
			self.mane_delay=random.randint(2,70)
			strip.setPixelColorRGB(self._LED_MANE,255,255,255)
			strip.setPixelColorRGB(self._LED_MANE+1,255,255,255)
			strip.setPixelColorRGB(self._LED_MANE+2,255,255,255)
		else:
			strip.setPixelColorRGB(self._LED_MANE,0,255,int(math.sin(time.time()*2.7)*50.+50.))
			strip.setPixelColorRGB(self._LED_MANE+1,0,255,int(math.sin(time.time()*3.5)*50.+50.))
			strip.setPixelColorRGB(self._LED_MANE+2,0,255,int(math.sin(time.time()*4.5)*50.+50.))
		#let horn pulsate in red
		strip.setPixelColorRGB(self._LED_HORN,0,int(math.sin(time.time()*6)*127.+127.),0)
		#eyes flicker in different red/pink tones
		r=random.randint(50,255)
		b=random.randint(0,r>>2)
		strip.setPixelColorRGB(self._LED_EYES,0,r,b)
		strip.setPixelColorRGB(self._LED_EYES+1,0,r,b)
		#now pump the colors into the strip via SPI
		strip.show()

	def update(self):
		pass

	def shutdown(self):		#on closing set everything back to black
		global strip
		for i in range(0, self._LED_COUNT):
			strip.setPixelColorRGB(i, 0, 0, 0)
		strip.show()

