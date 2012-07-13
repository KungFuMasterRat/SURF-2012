##Converting polar to cartesian 

import math

def polar2cart(r, theta):
    ##Conversion formulas
    theta = theta * math.pi / 180.0
    x = r*math.cos(theta)
    y = r*math.sin(theta)
    return x, y


print polar2cart(1, 0) == (1, 0)
print polar2cart(1, 0)
print polar2cart(1, 90) == (0, 1)
print polar2cart(1, 90)
print polar2cart(1, 180) == (-1, 0)
print polar2cart(1, 180)
