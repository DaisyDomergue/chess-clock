from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep
from timer import timer
from gpiozero import LED, Button
from signal import pause

class Chess_clock(object):

    def __init__(self,time):
        super(Chess_clock, self).__init__()    
        self.WHITES_TURN = 1
        self.BLACKS_TURN = 0

        self.turn = self.WHITES_TURN
        
        self.time_black = timer("white",600)
        self.time_white = timer("black",600)

        self.led = LED(17)       # define LED pin according to BCM Numbering
        self.button = Button(18) # define Button pin according to BCM Numbering
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
        self.lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)
        mcp.output(3,1)     # turn on LCD backlight
        self.lcd.begin(16,2)     # set number of LCD lines and columns
        self.button.when_pressed = self.onButtonPressed


    time_white = None
    time_black = None

    def toggleLED(self):
        if self.led.is_active:
            print("Switching off")
            self.led.off()
        else:
            print("Switching on")
            self.led.on()

    def onButtonPressed(self):
        self.toggleLED()
        print("Button is pressed, led toggled >>>")
        if self.turn:
            self.turn = self.BLACKS_TURN
        else:
            self.turn = self.WHITES_TURN
      
def loop (self):
    while self.time_white.getTime() > 0 or self.time_black.getTime() > 0:
        print("looping timers set at : " + str(self.time_white.getTime()) + "," + str(self.time_black.getTime()))    
        self.lcd.setCursor(0,0)
        self.lcd.message('White:     ' + self.time_white.getFormatedTime() + '\n')
        self.lcd.message('Black:     ' + self.time_black.getFormatedTime() )
        if self.turn:
            self.time_white.decrement_second()
        else:
            self.time_black.decrement_second()
        sleep(1)
        
def destroy(self):
    self.lcd.clear()
if __name__ == '__main__':
    print ('Program is starting ... ')
    t = 600
    clock = Chess_clock(t)

    try:
        loop(clock)
    except KeyboardInterrupt:
        destroy(clock)