'''
Play a sequence of colors on a NeoPixel LED connected to GPIO16. The colors are defined in the 'play' string and their corresponding RGB values are stored in the 'colors' dictionary. The LED will change color every second according to the sequence.
(for RP2040-zero with CircuitPython)
'''
import board            # board description
import neopixel         # LED control library
from time import sleep

# get an LED controller for one LED connected to pin 16
ledPin = board.GP16
led = neopixel.NeoPixel(ledPin, 1)

#(Red, Green, Blue) values for each color
colors = { 
    'R': (255,0,0),     #red 
    'G': (0,255,0),     #green
    'B': (0,0,255),     #blue
    'C': (0,255,255),   #cyan
    'M': (255,0,255),   #magenta
    'Y': (255,128,0),       #black/off
    '_': (0,0,0),       #black/off
    'W': (255,255,255), #white
    'O': (255,165,0),   #orange
    'P': (128,0,128),   #purple
    'L': (255,255,224), #linen
    'D': (128,128,128)  #dark gray
}

#list of colors to play
play = 'RWB_BWR_GCMYK_' #see colors dictionary below for the color codes

while True:
    for p in play:
        print(f"Playing color: {p} - {colors[p]}") #print the color being played
        led.fill(colors[p])    #look up the color from the letter and queue the first LED value
        sleep(1)
