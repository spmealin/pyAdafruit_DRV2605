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

# I2C trigger by sending 'go' command
drv.setMode(DRV2605_MODE_INTTRIG)  # default, internal trigger when sending GO command

drv.selectLibrary(1)
drv.setWaveform(0, 84)  # ramp up medium 1, see datasheet part 11.2
drv.setWaveform(1, 1)  # strong click 100%, see datasheet part 11.2
drv.setWaveform(2, 0)  # end of waveforms

### loop ###
while(True):
	drv.go()
	time.sleep(1)
# end while(True)
