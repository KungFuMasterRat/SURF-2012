""" Simple pygame example.

Taken from:
http://www.swharden.com/blog/2010-06-15-simplest-case-pygame-example/
"""


import pygame  ##always import modules that you are using
import sys
import time
import random
import math
import pygame.display
import pygame.camera




pygame.init()  # load pygame modules ##Initialize itself

##pygame.camera.init()
##cam =pygame.camera.Camera(0)
##cam.start()


size = width, height = 300, 240  # size of window ##Arg unpack

speed = [4, 4]  # speed and direction ##Speed dx and dy

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)  # make window ## set the size of its screen

s_size = s_width, s_height = 100, 50
s = pygame.Surface(s_size)  # create surface 100px by 50px ##new surface; this is the actual 'physical' box
##S is defined in pygame; it is an object and class is pygame.Surface
s.fill((255, 160, 0))  # color the surface blue #RGB values to color the box
##Actually a method. Functions attached to objects =def
r = s.get_rect()  # get the rectangle bounds for the surface
##another method. Returns the rectangular bound. Surface has a color and this is the actual bounding of the object
clock = pygame.time.Clock()  # make a clock
##how often you redraw the frames; nothing to do with the speed, just frame rate

##defined four functions:
def handle_events(): #handles events: while it goes it the animate loop
    for event in pygame.event.get():  # if something clicked ##event is an object of some type defined. pygame event
        if event.type == pygame.QUIT:  # if EXIT clicked ##Type is the pygame type
            sys.exit()  # close cleanly
       
        if (event.type == pygame.KEYUP) or (event.type == pygame.KEYDOWN) :
            print event
            if (event.key == pygame.K_ESCAPE):
           			sys.exit()

_last_called = time.time()
_last_theta = 0 
def polar2cart(r, theta):
    ##Conversion formulas
    theta = theta * math.pi / 180.0
    x = r*math.cos(theta)
    y = r*math.sin(theta)
    return x, y
def animate():
    global r
    global _last_called
    global _last_theta
    
    now = time.time()
    if now - _last_called > .25:  # 2 is in seconds
        # Remember when I was called last
        _last_called = now  ##appears every 2 seconds (goes through 60x)

        _last_theta = _last_theta + 15
        theta = _last_theta
        x, y = polar2cart(50, theta)
        x+= 150
        y+=100
        
        print theta, x, y 
        
        # pygame.Rect needs 'left', 'top', 'width', 'height'
        # The 100, and the 50 are borrowed from the Surface above
        r = pygame.Rect(x, y, s_width, s_height)

def redraw(): #once we move box, we redraw screen, erase screen, redraw box in new position
    screen.fill((0, 0, 0))  # make redraw background black ##draws a black box
    screen.blit(s, r)  # render the surface into the rectangle ##blit is to put it on the screen. takes surface and shape, saws draw surface at this position
    pygame.display.flip()  # update the screen ##dual screen that flips back and forth


def main(): ##What tells it to move 30 times a sec
    ##i= 0
    while 1:  # infinite loop
        clock.tick(30)  # limit framerate to 30 FPS ##clock object prv def.

        handle_events() ##associated with clock.tickstops you from faster 30x a sec; it's s throttle to remember when it needs to refresh itself
        animate()  ##this function calls these three functions we prv def.
        redraw()
       ## saveimage(i)
        ##i = i + 1
##def saveimage(frame_number): ##Saves each frame
  ##  image = cam.get_image()
    ##pygame.image.save(image, 'frame_%i.jpg' % frame_number)
# DO IT!
main() ##last thing is call main, which starts the whole thing
