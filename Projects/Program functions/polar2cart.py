##Converting polar to cartesian 

import math
import time

def polar2cart(r, theta):
    ##Conversion formulas
    theta = theta * math.pi / 180.0
    x = r*math.cos(theta)
    y = r*math.sin(theta)
    return x, y

r = 1
for theta in range(0, 360, 5):
    print r, theta, polar2cart(r, theta)
    time.sleep(0.1)
