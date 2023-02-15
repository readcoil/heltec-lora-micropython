import ssd1306
from machine import SoftI2C, Pin
import time

def init_oled():
	rst = Pin(16, Pin.OUT)
	rst.value(1)
	scl = Pin(15, Pin.OUT, Pin.PULL_UP)
	sda = Pin(4, Pin.OUT, Pin.PULL_UP)
	i2c = SoftI2C(scl=scl, sda=sda, freq=450000)
	oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)
	test_screen(oled)
	screen = [" "," "," "," "," "]
	return oled, screen
	
def write_screen(oled, screen):
	oled.fill(0)
	for row, text in enumerate(screen):
		print(f"{row} - {text}")
		line = 12 * row
		oled.text(text, 0, line, 1)
	oled.show()
	
def test_screen(oled):
	oled.fill(0)
	oled.fill_rect(0, 0, 32, 32, 1)
	oled.fill_rect(2, 2, 28, 28, 0)
	oled.vline(9, 8, 22, 1)
	oled.vline(16, 2, 22, 1)
	oled.vline(23, 8, 22, 1)
	oled.fill_rect(26, 24, 2, 4, 1)
	oled.text('MicroPython', 40, 0, 1)
	oled.text('SSD1306', 40, 12, 1)
	oled.text('OLED 128x64', 40, 24, 1)
	oled.text(str(int(time.time())),40, 36, 1)
	oled.show()
	
	time.sleep(3)
	oled.fill(0)
	oled.show()
