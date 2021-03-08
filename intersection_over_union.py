#https://scipython.com/book/chapter-8-scipy/problems/p84/overlapping-circles/

import numpy as np
import math


def intersection_area(x1,y1,R,x2,y2,r):
    """Return the area of intersection of two circles.

    The circles have radii R and r, and their centres are separated by d.

    """
    d = find_d(x1, y1, x2, y2)
    if d <= abs(R-r):
        # One circle is entirely enclosed in the other.
        return np.pi * min(R, r)**2
    if d >= r + R:
        # The circles don't overlap at all.
        return 0

    r2, R2, d2 = r**2, R**2, d**2
    alpha = np.arccos((d2 + r2 - R2) / (2*d*r))
    beta = np.arccos((d2 + R2 - r2) / (2*d*R))
    return ( r2 * alpha + R2 * beta -
             0.5 * (r2 * np.sin(2*alpha) + R2 * np.sin(2*beta))
           )

def find_d(x1,y1,x2,y2):
    return math.sqrt(pow(x1-x2,2) + pow(y1-y2,2))

def union_area(x1,y1,r1,x2,y2,r2):
    d = find_d(x1, y1, x2, y2)
    if d <= abs(r1-r2):
        # One circle is entirely enclosed in the other.
        return np.pi * min(r1, r2)**2
    if d >= r1 + r2:
        # The circles don't overlap at all.
        return 0

    area1= math.pi * pow(r1,2)
    area2 = math.pi * pow(r2, 2)

    intersection= intersection_area(x1,y1,r1,x2,y2,r2)

    return area1 + area2 - intersection


if __name__ =='__main__':
    union= union_area(234,230,56,248,232,221)
    print(union)
    intersection = intersection_area(234,230,56,248,232,221)
    print(intersection)