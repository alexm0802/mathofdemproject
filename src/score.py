#Currently, there isn't really a way to test this code, so there could be a lot
#of errors...
#also, we are using dem+rep, instead of total to ignore idependent voters (but add extra noise)
#for the sake of the statistical stuff
import numpy as np
import math

def get_column(col_num, data):
    column = []
    for i in range (0, len(data)):
        row = data[i]
        column.append(row[col_num])
    return column

def prob (percent_r):
	return 1/(1+math.exp(-0.7*(percent_r*100-50)))

def calc_score (n_map, county_data):
    ideal_breakdown = sum(list(map(int, get_column(2, county_data))))/(sum(list(map(int, get_column(2, county_data))))+sum(list(map(int, get_column(3, county_data)))))
    score = 0
    georgia_pop = 0
    for i in n_map:
        dist_pop = 0
        dist_percentr = 0
        for j in i:
        	names = get_column(0, county_data)
        	index = names.index(j)
        	dist_pop += int(county_data[index][2]) + int(county_data[index][3])
        	dist_percentr += int(county_data[index][2])
        dist_percentr = dist_percentr/dist_pop
        georgia_pop += dist_pop
        score += prob(dist_percentr)*dist_pop
    score = score/georgia_pop
    print('ideal_breakdown: ', ideal_breakdown)
    print('breakdown of districts: ', score)

g = open('data/map.txt')
n_map = []
for line in g:
	temp = line.split(', ')
	del temp[len(temp)-1]
	n_map.append(temp)
county_data = [] #county_data[0]=names, county_data[1]=total votes
                #county_data[2]=rep votes, county_data[4]= dem votes
g.close()
f = open('data/georgia_2012_results.csv', 'r')
for line in f:
	temp = line.split(',')
	county_data.append([temp[2], temp[7], temp[4], temp[5]])
f.close()
calc_score(n_map, county_data)