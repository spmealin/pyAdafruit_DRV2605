# About

This is a python module for the Adafruit DRV2605L Haptic Driver, based on the exhalent library supplied by Adafruit.  The original library has been ported to python so it can run on the BeagleBone Black, http://beagleboard.org/BLACK.

The original Arduino library, written by Limor Fried/Ladyada for Adafruit Industries, can be found at https://github.com/adafruit/Adafruit_DRV2605_Library.

The Adafruit DRV2605L project page on Adafruit can be found at http://www.adafruit.com/products/2305.

The Adafruit tutorial for the Arduino can be found at https://learn.adafruit.com/adafruit-drv2605-haptic-controller-breakout.

The python code was written by Sean Mealin.

# Requirements

This python module depends on Adafruit's BeagleBone IO Python Library, which can be found at https://github.com/adafruit/adafruit-beaglebone-io-python.  

It has been tested on Ubuntu with kernel 3.8 and above, and newer versions of python 2.7.

# Hardware Setup

The driver uses I2C to communicate with the BeagleBone Black.  Connect it using I2C 1 (pins P9_17, P9_18) or I2C 2 (pins P9_19, P9_20).  You may have to enable I2C depending on your operating system (Debian, Ubuntu, etc) and your kernel version (3.8, 3.14, etc).  Don't forget about power and ground.  More wiring information can be found at https://learn.adafruit.com/adafruit-drv2605-haptic-controller-breakout.  The information there is shown using the Arduino, but the same wiring principles apply.

# Usage

Insure that Adafruit_DRV2605.py is in the same directory as your python script, and import it using the normal python import mechanisms.  For example, copy examples/basic/basic.py and Adafruit_DRV2605.py to the same directory, and run basic.py with the following command:

`python basic.py`

# Disclaimer

This code and any information is provided as is.  The author, Sean Mealin, has attempted to follow the original Arduino code as closely as possible.  Any problems or errors were made by the author, and do not reflect on Adafruit in any way.

As with the original Arduino library, this code is distributed under the MIT license.