import numpy as np
from graphics import *

def is_numeric(s):
    s = s.replace ('-','')
    s = s.replace (' ','')
    s = s.replace ('\n','')
    s = s.replace ('.','')
    return s.isdigit()

def draw_county(county):
    f = open('data/georgia_county_locations.txt', 'r')
    xcoord = []
    ycoord = []
    while True:
        temp = f.readline()
        temp = temp.replace ('\n','')
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
    vertices = []
    for i in range(0, len(xcoord)):
        p = Point(((float(xcoord[i]) - float(xmin))/x_range)*x_length,
        y_length-((float(ycoord[i]) - float(ymin))/y_range)*y_length)
        vertices.append(p)
    n = Polygon(vertices)
    n.setFill('white')
    n.setOutline('black')
    n.setWidth(2)
    n.draw(win)
    f.close()

xmax = -80.841255
xmin = -85.605202
ymax = 35.000683
ymin = 30.355408
x_range = float(xmax) - float(xmin)
y_range = float(ymax) - float(ymin)
x_length = 500
y_length = abs(x_length*y_range/x_range)
win = GraphWin('Georgia', x_length, y_length)

g = open('data/ga_counties.txt', 'r')
for line in g:
    line = line.split()
    county_name = ''
    for i in line:
        if (i == "County"):
            county_name = county_name[:-1] #fencepost error
            draw_county(county_name)
        else:
            county_name += i + ' '
g.close()
win.getMouse()
win.close()
