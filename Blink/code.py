'''
Blink an LED
Board: RP2040-zero, with WS2821 LED on pin 16
'''
import board            # board description
import neopixel         # LED control library
from time import sleep

# get an LED controller for one LED connected to pin 16
ledPin = board.GP16
led = neopixel.NeoPixel(ledPin, 1)

while True:
    print("Blink!")
    color0 = (255, 0, 0)  #(red, green, blue)
    led.fill(color0)
    sleep(0.5)

    color1 = (0, 0, 0)
    led.fill(color1)
    sleep(0.5)
