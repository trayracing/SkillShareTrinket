'''
Blink an LED
Board: RP2040-zero, with WS2821 LED on pin 16
'''
import board            # board decription
import neopixel         # LED control library
from time import sleep

# Connect an LED strip to Pin 11 with 5V power and ground.
ledPin = board.GP11
pixels = neopixel.NeoPixel(ledPin, 5, brightness=.2,pixel_order=neopixel.RGB)

# This is defining some basic colors
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
WHITE=(255,220,160)
BLACK=(0,0,0)


while True:
    pixels[0]=RED
    pixels[1]=GREEN
    pixels[2]=BLUE
    pixels[3]=YELLOW
    pixels[4]=WHITE  
    pixels.show()
    sleep(0.5)

    pixels.fill(BLACK)
    sleep(0.5)
