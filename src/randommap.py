from adjacentcounty import get_adjacent_counties
import numpy as np
f = open('data/georgia_2012_results.csv', 'r')
f.readline()
county_data = [] #county_data[0]=names, county_data[1]=total votes
                    #county_data[2]=rep votes, county_data[4]= dem votes
for line in f:
    temp = line.split(',')
    county_data.append([temp[2], temp[7], temp[4], temp[5]])
maps = []
scores = []
print(county_data)
counties_data = county_data
total_state_voting_population = -1
for i in range(0, len(county_data)):
	total_state_voting_population = total_state_voting_population + int(county_data[i][1])
print(total_state_voting_population)
NUM_DISTRICTS = 14
ideal_district_size = total_state_voting_population/NUM_DISTRICTS
print(ideal_district_size)
#large districts: Fulton, Gwinnett, Cobb, DeKalb
districts = []
pop_already_districted = 0
last_county = len(county_data) - 1
print(last_county)
print(county_data[last_county])
for j in range(0, last_county):
	if j < len(county_data) :
		county_size = county_data[j][1]
		if int(county_size) >= ideal_district_size:
			districts.append(county_data[j][0])
			pop_already_districted = int(pop_already_districted) + int(county_data[j][1])
			county_data.remove(county_data[j])
mod_ideal_size = (total_state_voting_population - pop_already_districted)/(NUM_DISTRICTS - len(districts))
mod_size_ceiling = 1.1*mod_ideal_size
mod_size_floor = 0.9*mod_ideal_size
print(mod_ideal_size)
print(districts)
for i in range(0, len(county_data)):
	if i < len(county_data):
		district_pop = 0
		counties_in_district = []
		district_pop = int(county_data[i][1])
		county_name = county_data[i][0]
		counties_in_district.append(county_name)
		county_data.remove(county_data[i])
		adjacent_counties = get_adjacent_counties(county_name)
		#print(adjacent_counties)
		while district_pop < mod_size_floor:
			random_county_index = -1
			while random_county_index == -1:
				random_ceiling = len(adjacent_counties)
				random_int = np.random.randint(0, random_ceiling)
				random_county_name = adjacent_counties[random_int]
				print(random_county_name)
				print(districts)
				print(adjacent_counties)
				print(counties_in_district)
				for j in range(0, len(county_data)):
					if county_data[j][0] == random_county_name:
						random_county_index = j
				for j in range(0, len(counties_in_district)):
					if counties_in_district[j] == random_county_name:
						random_ceil = len(counties_in_district)
						random_num = np.random.randint(0, random_ceil)
						adjacent_counties = get_adjacent_counties(counties_in_district[random_num])
			random_county_pop = int(county_data[random_county_index][1])
			random_data = county_data[random_county_index]
			if random_county_pop + district_pop < mod_size_ceiling:
				counties_in_district.append(random_county_name)
				county_data.remove(random_data)
				adjacent_counties = get_adjacent_counties(random_county_name)
				district_pop = district_pop + random_county_pop
				#print(adjacent_counties)
			elif random_ceiling == 1:
				print("only one adjacent county and it's 2 big")
				counties_in_district.append(random_county_name)
				county_data.remove(random_data)
				adjacent_counties = get_adjacent_counties(random_county_name)
				district_pop = district_pop + random_county_pop
				#print(adjacent_counties)
			if(len(districts)>13):
				break
		districts.append(counties_in_district)
		print(districts)

print("DISTRICTS MADE")	
print(districts)


