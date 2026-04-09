'''
Blink an LED
Board: RP2040-zero, with WS2821 LED on pin 16
'''
import board            # board decription
import neopixel         # LED control library
from time import sleep

# get an LED controller for one LED connected to pin 16
ledPin = board.GP16
led = neopixel.NeoPixel(ledPin, 1, brightness=.2)

# Extra setup for a switch connected between Pin 14 and Ground
import digitalio
buttonPin = board.GP14
button = digitalio.DigitalInOut(buttonPin)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# This is defining some basic colors
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
WHITE=(255,220,160)
BLACK=(0,0,0)


while True:
    # Choose to RED or GREEN depending on whether the button is pressed
    if button.value: # The button is not pressed
        led.fill(RED)
    else: # The button is pressed
        led.fill(GREEN)

    sleep(0.5)
    led.fill(WHITE)
    sleep(0.5)
