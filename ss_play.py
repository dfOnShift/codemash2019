'''
star spangled banner on Circuit Playground Express using Circuit Python

'''

from adafruit_circuitplayground.express import cpx

# color palette for NeoPixels
red = (30, 00, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
pink = (255, 0, 255)
dark = (0,0,0)

# NeoPixel blank out
cpx.pixels.fill( dark )

# set global brightness
cpx.pixels.brightness = 0.05

# The frequency of the tones in Hz
Note1=233
Note2=294
Note3=330
Note4=349
Note5=392
Note6=440
Note7=466
Note8=523
Note9=587
Note10=622
Note11=698

def color_piano(htz, time, color): #frequency, time, color
    cpx.play_tone(htz, time)
    cpx.pixels.fill( color )

def star_spangled_banner():
    t = 0.5 # time multiplier
    color_piano(Note4, t*0.75, red)
    color_piano(Note2, t*0.25, white)
    color_piano(Note1, t*1, red)
    color_piano(Note2, t*1, white)
    color_piano(Note4, t*1, red)
    color_piano(Note7, t*2, white)
    color_piano(Note9, t*0.75, blue)
    color_piano(Note8, t*0.25, white)
    color_piano(Note7, t*1, red)
    color_piano(Note2, t*1, white)
    color_piano(Note3, t*1, blue)
    color_piano(Note4, t*2, red)
    color_piano(Note4, t*0.5, red)
    color_piano(Note4, t*0.5, red)

    color_piano(Note9, t*1.5, blue)
    color_piano(Note8, t*0.5, white)
    color_piano(Note7, t*1, red)
    color_piano(Note6, t*2, blue)
    color_piano(Note5, t*0.5, white)
    color_piano(Note6, t*0.5, blue)
    color_piano(Note7, t*1, red)
    color_piano(Note7, t*1, red)
    color_piano(Note4, t*1, blue)
    color_piano(Note2, t*1, white)
    color_piano(Note1, t*1, blue)
    color_piano(Note4, t*0.75, red)
    color_piano(Note2, t*0.25, white)

    color_piano(Note1, t*1, red)
    color_piano(Note2, t*1, white)
    color_piano(Note4, t*1, red)
    color_piano(Note7, t*2, white)
    color_piano(Note9, t*0.75, blue)
    color_piano(Note8, t*0.25, white)
    color_piano(Note7, t*1, red)
    color_piano(Note2, t*1, white)
    color_piano(Note3, t*1, blue)
    color_piano(Note4, t*2, red)
    color_piano(Note4, t*0.5, red)
    color_piano(Note4, t*0.5, red)

    color_piano(Note9, t*1.5, blue)
    color_piano(Note8, t*0.5, white)
    color_piano(Note7, t*1, red)
    color_piano(Note6, t*2, blue)
    color_piano(Note5, t*0.5, white)
    color_piano(Note6, t*0.5, blue)
    color_piano(Note7, t*1, red)
    color_piano(Note7, t*1, red)
    color_piano(Note4, t*1, blue)
    color_piano(Note2, t*1, white)
    color_piano(Note1, t*1, red)
    color_piano(Note9, t*0.5, blue)
    color_piano(Note9, t*0.5, blue)

    color_piano(Note9, t*1, blue)
    color_piano(Note10, t*1, red)
    color_piano(Note11, t*1, white)
    color_piano(Note11, t*2, white)
    color_piano(Note10, t*0.5, red)
    color_piano(Note9, t*0.5, blue)
    color_piano(Note8, t*1, white)
    color_piano(Note9, t*1, blue)
    color_piano(Note10, t*1, red)
    color_piano(Note10, t*2, red)
    color_piano(Note10, t*1, red)

    color_piano(Note9, t*1, white)
    color_piano(Note8, t*0.5, blue)
    color_piano(Note7, t*1, white)
    color_piano(Note6, t*2, red)
    color_piano(Note5, t*0.5, blue)
    color_piano(Note6, t*0.5, red)
    color_piano(Note7, t*1, white)
    color_piano(Note2, t*1, blue)
    color_piano(Note3, t*1, red)
    color_piano(Note4, t*2, white)
    color_piano(Note4, t*1, red)

    t=t*1.08
    color_piano(Note7, t*1, white)
    color_piano(Note7, t*1, white)
    color_piano(Note7, t*0.5, white)
    color_piano(Note6, t*0.5, blue)
    color_piano(Note5, t*1, red)
    color_piano(Note5, t*1, red)
    color_piano(Note5, t*1, red)
    color_piano(Note8, t*1, white)
    color_piano(Note10, t*0.5, red)
    color_piano(Note9, t*0.5, blue)
    color_piano(Note8, t*0.5, white)
    color_piano(Note7, t*0.5, red)

    color_piano(Note7, t*1, red)
    color_piano(Note6, t*2, blue)
    color_piano(Note4, t*0.5, red)
    color_piano(Note4, t*0.5, red)
    color_piano(Note7, t*1.5, blue)
    color_piano(Note8, t*0.5, white)
    color_piano(Note9, t*0.5, blue)
    color_piano(Note10, t*0.5, red)

    t = t*1.2
    color_piano(Note11, t*2, white)
    color_piano(Note7, t*0.5, red)
    color_piano(Note8, t*0.5, white)
    color_piano(Note9, t*1.5, blue)
    color_piano(Note10, t*0.5, red)
    color_piano(Note8, t*1, white)
    color_piano(Note7, t*2, red)

while True:
    if cpx.touch_A4:
        cpx.pixels[0] = red
    if cpx.touch_A5:
        cpx.pixels[1] = red
        cpx.pixels[2] = white
    if cpx.touch_A6:
        cpx.pixels[3] = white
    if cpx.touch_A7:
        cpx.pixels[4] = white
    if cpx.touch_A1:
        cpx.pixels[5] = blue
        cpx.pixels[6] = blue
    if cpx.touch_A2:
        cpx.pixels[7] = blue
        cpx.pixels[8] = blue
    if cpx.touch_A3:
        cpx.pixels[9] = red
        cpx.red_led = 1
    if cpx.button_a:  # pink mode
        cpx.pixels.fill( pink )
        cpx.red_led = 0
    if cpx.button_a and cpx.button_b:  # play the star spangled banner
        star_spangled_banner()
        cpx.pixels.fill( dark )