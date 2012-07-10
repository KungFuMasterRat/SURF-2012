##Converting polar to cartesian 

import math

##Obtain polar coordinates from user
r = raw_input("Please enter the r coordinate: ")
theta = raw_input("Please enter the theta coordinate: ")

##Conversion formulas
x = r*cos(theta)
y = r*sin(theta)

##Output the results
print "The Cartesian coordinates for (",r",",theta,") are (",x,",",y,")