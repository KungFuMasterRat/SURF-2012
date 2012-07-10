""" Simple pygame example.

Taken from:
http://www.swharden.com/blog/2010-06-15-simplest-case-pygame-example/
"""


import pygame
import sys

pygame.init()  # load pygame modules ##Initialize itself

size = width, height = 1020, 240  # size of window ##Arg unpack

speed = [4, 4]  # speed and direction ##Speed dx and dy

screen = pygame.display.set_mode(size)  # make window ## set the size of its screen

s = pygame.Surface((100, 50))  # create surface 100px by 50px ##new surface; this is the actual 'physical' box
##S is defined in pygame; it is an object and class is pygame.Surface
s.fill((33, 66, 99))  # color the surface blue #RGB values to color the box
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


def animate(): ##new funnction called animate
    global r ##effects global/module-level namespace of r (prviously defined)
    r = r.move(speed)  # move the box by the "speed" coordinates

     # if we hit a  wall, change direction
    if r.left < 0 or r.right > width: #greater than width of screen; 0
        speed[0] = -speed[0] ##pong logic; neg is telling to flip but maintain speed
##can mult reversal speed to slow down
    if r.top < 0 or r.bottom > height:
        speed[1] = -speed[1] *0.99 ## 1 is the second item being called in dx dy


def redraw(): #once we move box, we redraw screen, erase screen, redraw box in new position
    screen.fill((0, 0, 0))  # make redraw background black ##draws a black box
    screen.blit(s, r)  # render the surface into the rectangle ##takes surface and shape, saws draw surface at this position
    pygame.display.flip()  # update the screen ##dual screen that flips back and forth


def main(): ##What tells it to move 30 times a sec
    while 1:  # infinite loop
        clock.tick(10)  # limit framerate to 30 FPS ##clock object prv def.

        handle_events() ##associated with clock.tickstops you from faster 30x a sec; it's s throttle to remember when it needs to refresh itself
        animate()  ##this function calls these three functions we prv def.
        redraw()

# DO IT!
main() ##last thing is call main, which starts the whole thing
