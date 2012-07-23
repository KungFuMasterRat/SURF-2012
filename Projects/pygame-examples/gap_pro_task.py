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


##Speed dx and dy of object
speed = [4, 4]  

## Size of object
s_size = s_width, s_height = 50, 50 #(How many pixels in a cm?) 


