##################################################
#  This is a library for the Adafruit DRV2605L Haptic Driver
#
#  ----> http://www.adafruit.com/products/2305
# 
#  Check out the links above for our tutorials and wiring diagrams
#  This motor/haptic driver uses I2C to communicate
#
#  Adafruit invests time and resources providing this open source code,
#  please support Adafruit and open-source hardware by purchasing
#  products from Adafruit!
#
#  Original Arduino library Written by Limor Fried/Ladyada for Adafruit Industries.
#  Python module written by Sean Mealin
#  MIT license, all text above must be included in any redistribution
##################################################

import time

from Adafruit_DRV2605 import *

drv = Adafruit_DRV2605(busnum=2)

### setup ###
drv.begin()
drv.selectLibrary(1)

# I2C trigger by sending 'go' command
# default, internal trigger when sending GO command
drv.setMode(DRV2605_MODE_INTTRIG)

effect = 1

### loop ###
while(True):
	print("Effect #" + str(effect))
	
	# set the effect to play
	drv.setWaveform(0, effect)  # play effect
	drv.setWaveform(1, 0)       # end waveform
	
	# play the effect!
	drv.go()
	
	# wait a bit
	time.sleep(0.5)
	
	effect+=1
	if(effect > 117):
		effect = 1
	# end if(effect
# end while(True)
