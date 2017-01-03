#This file will become a function that draws a county given an input color, and
#county name (assuming Georgia for everything)
#Currently, it will do a lot of extra stuff that will be unnecessary later

import numpy as np
from graphics import *

def is_numeric(s):
    s = s.replace ('-','')
    s = s.replace (' ','')
    s = s.replace ('\n','')
    s = s.replace ('.','')
    return s.isdigit()

f = open('data/georgia_county_locations.txt', 'r')
#print (f)
county = "Ware"
xcoord = []
ycoord = []
while True:
    temp = f.readline()
    temp = temp.replace ('\n','')
    print(temp, " == ", county)
    if (temp.lower() == county.lower()):
        f.readline()
        f.readline()
        f.readline()
        for line in f:
            if is_numeric(line):
                xcoord.append(line.split()[0])
                ycoord.append(line.split()[1])
            else:
                break
        break

x_range = float(max(xcoord)) - float(min(xcoord))
y_range = float(max(ycoord)) - float(min(ycoord))
x_length = 500
y_length = abs(x_length*y_range/x_range)
print(y_length)
win = GraphWin("County", x_length, y_length)

vertices = []
for i in range(0, len(xcoord)):
    p = Point(x_length-((float(xcoord[i]) - float(min(xcoord)))/x_range)*x_length,
    y_length-((float(ycoord[i]) - float(min(ycoord)))/y_range)*y_length)
    vertices.append(p)
n = Polygon(vertices)
n.setFill('pink')
n.setOutline('black')
n.setWidth(4)
n.draw(win)
win.getMouse()
win.close()
