from graphics import *
from score import *

def is_numeric(s):
    s = s.replace ('-','')
    s = s.replace (' ','')
    s = s.replace ('\n','')
    s = s.replace ('.','')
    return s.isdigit()

def draw_county(county, color):
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
    n.setFill(color)
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

county_data = [] #county_data[0]=names, county_data[1]=total votes
                #county_data[2]=rep votes, county_data[4]= dem votes
f = open('data/georgia_2012_results.csv', 'r')
for line in f:
	temp = line.split(',')
	county_data.append([temp[2], temp[7], temp[4], temp[5]])
f.close()
names = get_column(0, county_data)

fi = open('data/map.txt')
for line in fi:
	temp = line.split(', ')
	del temp[len(temp)-1]
	percentr = 0
	pop = 0
	for t in temp:
		index = names.index(t)
		percentr += int(county_data[index][2])
		pop += int(county_data[index][2])+int(county_data[index][3])
	percentr /= pop
	print(temp[0], ' percent r: ', percentr)
	probability = prob(percentr)
	r = probability * 255
	b = (1-probability) * 255
	color = color_rgb(r, 0, b)
	print(temp[0], ": ", probability)
	for u in temp:
		draw_county(u, color)

fi.close()
win.getMouse()
win.close()
