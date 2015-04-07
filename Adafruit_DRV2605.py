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

from Adafruit_I2C import Adafruit_I2C

DRV2605_ADDR = 0x5A

DRV2605_REG_STATUS = 0x00
DRV2605_REG_MODE = 0x01
DRV2605_MODE_INTTRIG = 0x00
DRV2605_MODE_EXTTRIGEDGE = 0x01
DRV2605_MODE_EXTTRIGLVL = 0x02
DRV2605_MODE_PWMANALOG = 0x03
DRV2605_MODE_AUDIOVIBE = 0x04
DRV2605_MODE_REALTIME = 0x05
DRV2605_MODE_DIAGNOS = 0x06
DRV2605_MODE_AUTOCAL = 0x07

DRV2605_REG_RTPIN = 0x02
DRV2605_REG_LIBRARY = 0x03
DRV2605_REG_WAVESEQ1 = 0x04
DRV2605_REG_WAVESEQ2 = 0x05
DRV2605_REG_WAVESEQ3 = 0x06
DRV2605_REG_WAVESEQ4 = 0x07
DRV2605_REG_WAVESEQ5 = 0x08
DRV2605_REG_WAVESEQ6 = 0x09
DRV2605_REG_WAVESEQ7 = 0x0A
DRV2605_REG_WAVESEQ8 = 0x0B

DRV2605_REG_GO = 0x0C
DRV2605_REG_OVERDRIVE = 0x0D
DRV2605_REG_SUSTAINPOS = 0x0E
DRV2605_REG_SUSTAINNEG = 0x0F
DRV2605_REG_BREAK = 0x10
DRV2605_REG_AUDIOCTRL = 0x11
DRV2605_REG_AUDIOLVL = 0x12
DRV2605_REG_AUDIOMAX = 0x13
DRV2605_REG_RATEDV = 0x16
DRV2605_REG_CLAMPV = 0x17
DRV2605_REG_AUTOCALCOMP = 0x18
DRV2605_REG_AUTOCALEMP = 0x19
DRV2605_REG_FEEDBACK = 0x1A
DRV2605_REG_CONTROL1 = 0x1B
DRV2605_REG_CONTROL2 = 0x1C
DRV2605_REG_CONTROL3 = 0x1D
DRV2605_REG_CONTROL4 = 0x1E
DRV2605_REG_VBAT = 0x21
DRV2605_REG_LRARESON = 0x22

class Adafruit_DRV2605(object):
	def __init__(self, busnum=1):
		self.i2c = Adafruit_I2C(DRV2605_ADDR, busnum=busnum)
	# end def
	
	def begin(self):
		id = self.readRegister8(DRV2605_REG_STATUS)
		
		self.writeRegister8(DRV2605_REG_MODE, 0x00) # out of standby
		
		self.writeRegister8(DRV2605_REG_RTPIN, 0x00) # no real-time-playback
		
		self.writeRegister8(DRV2605_REG_WAVESEQ1, 1) # strong click
		self.writeRegister8(DRV2605_REG_WAVESEQ2, 0)
		
		self.writeRegister8(DRV2605_REG_OVERDRIVE, 0) # no overdrive
		
		self.writeRegister8(DRV2605_REG_SUSTAINPOS, 0)
		self.writeRegister8(DRV2605_REG_SUSTAINNEG, 0)
		self.writeRegister8(DRV2605_REG_BREAK, 0)
		self.writeRegister8(DRV2605_REG_AUDIOMAX, 0x64)
		
		# ERM open loop
		
		# turn off N_ERM_LRA
		self.writeRegister8(DRV2605_REG_FEEDBACK, self.readRegister8(DRV2605_REG_FEEDBACK) & 0x7F)
		# turn on ERM_OPEN_LOOP
		self.writeRegister8(DRV2605_REG_CONTROL3, self.readRegister8(DRV2605_REG_CONTROL3) | 0x20)
		
		return True
	# end def
	
	def setWaveform(self, slot, w):
		self.writeRegister8(DRV2605_REG_WAVESEQ1+slot, w)
	# end def
	
	def selectLibrary(self, lib):
		self.writeRegister8(DRV2605_REG_LIBRARY, lib)
	# end def
	
	def go(self):
		self.writeRegister8(DRV2605_REG_GO, 1)
	# end def
	
	def setMode(self, mode):
		self.writeRegister8(DRV2605_REG_MODE, mode)
	# end def
	
	def readRegister8(self, reg):
		return self.i2c.readU8(reg)
	# end def
	
	def writeRegister8(self, reg, val):
		self.i2c.write8(reg, val)
	# end def
# end class
