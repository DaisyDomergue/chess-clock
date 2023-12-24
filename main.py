from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep

PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
# Create PCF8574 GPIO adapter.
try:
    mcp = PCF8574_GPIO(PCF8574_address)
except:
    try:
        mcp = PCF8574_GPIO(PCF8574A_address)
    except:
        print ('I2C Address Error !')
        exit(1)
# Create LCD, passing in MCP GPIO adapter.
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)
mcp.output(3,1)     # turn on LCD backlight
lcd.begin(16,2)     # set number of LCD lines and columns


time_white = "00:00"
time_black = "00:00"

         
def loop(t):
    while t:
        lcd.setCursor(0,0)
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs)

        lcd.message('White:     ' + timer + '\n')
        lcd.message('Black:     ' + timer + '\n')
        t -= 1
        sleep(1)
def destroy():
    lcd.clear()
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop(int(600))
    except KeyboardInterrupt:
        destroy()