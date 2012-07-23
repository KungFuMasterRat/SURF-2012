##Gap prosaccade task

#Modules
import pygame  
import sys
import time
import random
import math
import pygame.display
import pygame.camera


#Initialize
pygame.init()

#Window size 
size = width, height = 1000, 600

##To make fullscreen
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)  # make window ## set the size of its screen

## Properties of object
speed = [4, 4]
s_size = s_width, s_height = 50, 50 #(How many pixels in a cm?) 
s = pygame.Surface(s_size) 
s.fill((255, 160, 0))
r = s.get_rect() 

##Makes a clock
clock = pygame.time.Clock() 


##Functions

def handle_events(): #To close from full screen
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            sys.exit()  # close cleanly
       
        if (event.type == pygame.KEYUP) or (event.type == pygame.KEYDOWN) : ##To close using escape key
            print event
            if (event.key == pygame.K_ESCAPE): 
           			sys.exit() ## Close cleanly
					
_last_called = time.time()
_last_theta = 0 

def PeripheralTargetDistance(viewingDistance, degVisAng):
    ##Conversion for viewing distance to peripheral. 
    degVisAng = degVisAng * math.pi / 180.0
    periphDistance = viewingDistance*math.tan(degVisAng)
   
    return periphDistance

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
	r = pygame.Rect(x, y, s_width, s_height)

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
main() ##last thing is 
