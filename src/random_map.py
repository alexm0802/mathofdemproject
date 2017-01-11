import numpy as np
from random import randint



def are_these_counties_adjacent(county1, county2, county_names):
	print(len(county_names))
	index_of_county_1 = -1
	index_of_county_2 = -1
	for i in range(0, len(county_names)):
		if county_names[i] == county1:
			index_of_county_1 = i
	for i in range(0, len(county_names)):
		if county_names[i] == county2:
			index_of_county_2 = i
	print(index_of_county_1)
	print(index_of_county_2)
	if index_of_county_1 == -1 or index_of_county_2 == -1:
		print("one or more county names invalid. try again")
		return
	else:
		adj_counties = adjacent_counties[index_of_county_1]
		for i in range(0, len(adj_counties)):
			if adj_counties[i] == county2:
				return True
		return False

def getpop (dist_name, county_data):
    for i in county_data:
    	if (dist_name==i[0]):
    		return int(i[1])
    return 0

def borders (county, district, county_names):
	print('borders')
	if(len(district) > 0):
		for i in district:
			if (are_these_counties_adjacent(county, i, county_names)):
				return True
		return False
	return True

def poach (i, districts):
	print('wehaf')

def randommap ():
    f = open('data/georgia_2012_results.csv', 'r')
    f.readline()
    county_data = [] #county_data[0]=names, county_data[1]=total votes
                    #county_data[2]=rep votes, county_data[4]= dem votes
    for line in f:
        temp = line.split(',')
        county_data.append([temp[2], temp[7], temp[4], temp[5]])

    total_state_voting_population = 0
    for i in range(0, len(county_data)):
	       total_state_voting_population += int(county_data[i][1])
    print(total_state_voting_population)
    NUM_DISTRICTS = 14
    ideal_district_size = total_state_voting_population/NUM_DISTRICTS
    print(ideal_district_size)
    remaining_dist = []
    county_names = []
    for i in county_data:
    	remaining_dist.append(i[0])
    	county_names.append(i[0])
    districts = []
    still_wrong = True
    while(still_wrong):
        for i in range(0, NUM_DISTRICTS):
        	dist = []
        	dist_pop = 0
        	contin = True
        	while (abs(dist_pop - ideal_district_size) > 10000 & contin):
        		if (dist_pop < ideal_district_size):
        			options = []
        			for i in remaining_dist:
        				options.append(i)
        			cont = True
        			while (cont):
        				rand = randint(0,len(options) - 1) #testing -1
        				print('rand= ', rand)
        				print('remainging dists length: ', len(remaining_dist))
        				print(options)
        				new_county = options[rand]
        				if (len(options) == 0):
        					print('fuck')
        					poach(dist, districts)
        					cont = False
        				print(new_county)
        				print(dist)
        				print(borders(new_county, dist, county_names))
        				if(borders(new_county, dist, county_names)):
        					dist.append(new_county)
        					remaining_dist.remove(new_county)
        					dist_pop += getpop(new_county, county_data)
        					cont = False
        					print('added county')
        				else:
        					#print(options)
        					print('options length ', len(options))
        					options.remove(new_county)
        		elif (dist_pop > ideal_district_size):
        			print('too big')
        			contin = False
        	districts.append(dist)

print('start')
f2 = open ('adjacent_countyinfo.txt')
adjacent_counties = []
for line in f2:
    temp = line.split(' ')
    temp.pop(0)
    adjacent_counties.append(temp)
randommap()
