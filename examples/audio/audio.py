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
print("DRV2605 Audio responsive test")
drv.begin()

drv.setMode(DRV2605_MODE_AUDIOVIBE)

# ac coupled input, puts in 0.9V bias
drv.writeRegister8(DRV2605_REG_CONTROL1, 0x20)

# analog input
drv.writeRegister8(DRV2605_REG_CONTROL3, 0xA3)

### loop ###
while(True):
	time.sleep(0)
# end while(True)
