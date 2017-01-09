from adjacentcounty import get_adjacent_counties
import numpy as np

print("run begins now")

f = open('data/georgia_2012_results.csv', 'r')
f.readline()
county_data = [] #county_data[0]=names, county_data[1]=total votes
                    #county_data[2]=rep votes, county_data[4]= dem votes
for line in f:
    temp = line.split(',')
    county_data.append([temp[2], temp[7], temp[4], temp[5]])

maps = []
backup_county_data = county_data
districts = []
multi_county_districts = []
scores = []
adjacent_counties = []
NUM_DISTRICTS = 14
pop_districted = 0

for i in range(0, len(county_data)):
	adjacent_counties.append(get_adjacent_counties(county_data[i][0]))

total_state_voting_population = -1
for i in range(0, len(county_data)):
	total_state_voting_population = total_state_voting_population + int(county_data[i][1])
ideal_district_size = total_state_voting_population/NUM_DISTRICTS

#does all the necessary things when a county is added to a district; it removes all references to it from certain arrays
#this makes sure a county won't be districted twice
def county_districted(county):
	county_index = get_county_data_index(county)
	adj_counties = []
	adj_counties = adjacent_counties[county_index]
	county_data.remove(county_data[county_index])
	adjacent_counties.remove(adj_counties)
	for i in range(0, len(adjacent_counties)):
		adj_counties_at_index = adjacent_counties[i]
		j = 0
		while j < len(adj_counties_at_index):
			if adj_counties_at_index[j] == county:
				adjacent_counties[i].remove(county)
			j = j+1

#this gets which multi county district a county belongs to
def get_multi_county_district_index(county):
	for i in range(0, len(multi_county_districts)):
		district_to_search = multi_county_districts[i]
		if len(district_to_search) == 4:
			print(district_to_search)
			print(county)
			if district_to_search == county:
				return i
		for j in range(0, len(district_to_search)):
			if district_to_search[j] == county:
				return i
	print("error - county cannot be found in a multi county district")
	print(county)
	return -1

def get_county_data_index(county):
	for i in range(0, len(county_data)):
		if county_data[i][0]==county:
			return i
	return -1


def seed_multi_county_districts():
	counties_districted = []
	while len(multi_county_districts) < NUM_MULTI_COUNTY_DISTRICTS:
		random_ceiling = len(county_data)
		random_int = np.random.randint(0, random_ceiling)
		if random_int < len(county_data):
			seed = county_data[random_int]
			district = []
			district.append(seed)
			multi_county_districts.append(district)
			counties_districted.append(seed)
			county_districted(seed[0])
	return counties_districted
	
def add_adjacent_counties(counties_recently_districted, looped):
	stuff_done = []
	for i in range(0, len(counties_recently_districted)):
		recent_county = counties_recently_districted[i]
		district_index = get_multi_county_district_index(recent_county)
		all_adj_counties = []
		all_adj_counties = get_adjacent_counties(recent_county[0])
		for j in range(0, len(all_adj_counties)):
			if j < len(all_adj_counties):
				county_index = get_county_data_index(all_adj_counties[j]) 
				if county_index != -1:
					multi_county_districts[district_index].append(county_data[county_index])
					stuff_done.append(county_data[county_index])
					county_districted(county_data[county_index][0])
	print(len(stuff_done))
	print(stuff_done)
	print(len(county_data))
	print(" counties left to be districted!")
	while len(county_data) > 0:
		add_adjacent_counties(stuff_done, looped)
"""
def add_adjacent_counties(counties_recently_districted, looped):
	stuff_done = []
	for i in range(0, len(counties_recently_districted)):
		recent_county = counties_recently_districted[i]
		district_index = get_multi_county_district_index(recent_county)
		all_adj_counties = []
		all_adj_counties = get_adjacent_counties(recent_county[0])
		for j in range(0, len(all_adj_counties)):
			if j < len(all_adj_counties):
				county_index = get_county_data_index(all_adj_counties[j]) 
				if county_index != -1:
					multi_county_districts[district_index].append(county_data[county_index])
					stuff_done.append(county_data[county_index])
					county_districted(county_data[county_index][0])
	print(len(stuff_done))
	print(stuff_done)
	print(len(county_data))
	print(" counties left to be districted!")
	while len(county_data) > 0:
		add_adjacent_counties(stuff_done, looped)

	while len(county_data) > 0 and looped < 10:
		looped += 1
		print("looped")
		print(looped)
		print("times")
		print(len(county_data))
		print(" counties left to be districted!")
		"""
	#add_adjacent_counties(stuff_done, looped)
#this makes each big county its own individual district
index = 0
while index < len(county_data):
	if float(county_data[index][1]) > ideal_district_size:
		districts.append(county_data[index])
		pop_districted = pop_districted + float(county_data[index][1])
		county_districted(county_data[index][0])
	index = index + 1

print("single county districts made ")
print(districts)

NUM_MULTI_COUNTY_DISTRICTS = 14
def make_districts():
	seedz = seed_multi_county_districts()
	print(len(seedz))
	print(seedz)
	add_adjacent_counties(seedz, 0)
	print(multi_county_districts)
	print(len(county_data))
	print(" counties left to be districted!")
	return multi_county_districts
d = make_districts()
def write_to_file(d):
	fi = open("data/map.txt", 'w')
	for i in range(0, len(multi_county_districts)):
		distr = multi_county_districts[i]
		for j in range(0, len(distr)):
			fi.write(distr[j][0])
			fi.write(", ")
		fi.write("\n")
write_to_file(d)
"""
#this seeds the 10 multi county districts with random districts
while len(multi_county_districts) < NUM_MULTI_COUNTY_DISTRICTS:
	random_ceiling = len(county_data)
	random_int = np.random.randint(0, random_ceiling)
	if random_int < len(county_data):
		seed = county_data[random_int]
		district = []
		district.append(seed)
		county_districted(seed[0])
		non_districted_near_counties = adjacent_counties[random_int]
		for j in range(0, len(non_districted_near_counties)):
			if j < len(non_districted_near_counties):
				county_to_append = non_districted_near_counties[j]
				district.append(county_data[get_county_data_index(county_to_append)])
				county_districted(non_districted_near_counties[j])
		multi_county_districts.append(district)
print("multi county districts seeded")
print(multi_county_districts)
print(len(county_data))
print(" counties left to be districted!")

for m in range(0, 10):
	for i in range(0, NUM_MULTI_COUNTY_DISTRICTS):
		county_in_question = multi_county_districts[i][1]
		non_districted_near_counties = adjacent_counties[get_county_data_index(county_in_question[0])]
		print(len(non_districted_near_counties))
		print(" is how many adjacent counties not yet districted there are")
		for j in range(0, len(non_districted_near_counties)):
			if j < len(non_districted_near_counties):
				county_to_append = non_districted_near_counties[j]
				multi_county_districts[i].append(county_data[get_county_data_index(county_to_append)])
				county_districted(non_districted_near_counties[j])
		
for i in range(0, NUM_MULTI_COUNTY_DISTRICTS):
	county_in_question = multi_county_districts[i][1]
	non_districted_near_counties = adjacent_counties[get_county_data_index(county_in_question[0])]
	print(len(non_districted_near_counties))
	print(" is how many adjacent counties not yet districted there are")
	for j in range(0, len(non_districted_near_counties)):
		if j < len(non_districted_near_counties):
			county_to_append = non_districted_near_counties[j]
			multi_county_districts[i].append(county_data[get_county_data_index(county_to_append)])
			county_districted(non_districted_near_counties[j])

print("multi county districts step 2 completed")
print(multi_county_districts)
print(len(county_data))
print(" counties left to be districted!")

for i in range(0, NUM_MULTI_COUNTY_DISTRICTS):
		#for k in range(0, len(multi_county_districts[i])):
		k = 0
		while k < len(multi_county_districts[i]):
			county_in_question = multi_county_districts[i][k]
			non_districted_near_counties = adjacent_counties[get_county_data_index(county_in_question[0])]
			for j in range(0, len(non_districted_near_counties)):
				if j < len(non_districted_near_counties):
					county_to_append = non_districted_near_counties[j]
					multi_county_districts[i].append(county_data[get_county_data_index(county_to_append)])
					county_districted(non_districted_near_counties[j])
			k = k + 1
print("step 2.5 done")
print(len(county_data))
print(" counties left to be districted!")
ind = 0
for m in range(0, 10):
	for i in range(0, NUM_MULTI_COUNTY_DISTRICTS):
		#for k in range(0, len(multi_county_districts[i])):
		k = 0
		while k < len(multi_county_districts[i]):
			county_in_question = multi_county_districts[i][k]
			non_districted_near_counties = adjacent_counties[get_county_data_index(county_in_question[0])]
			for j in range(0, len(non_districted_near_counties)):
				if j < len(non_districted_near_counties):
					county_to_append = non_districted_near_counties[j]
					multi_county_districts[i].append(county_data[get_county_data_index(county_to_append)])
					county_districted(non_districted_near_counties[j])
			k = k + 1
	print(len(county_data))
	print(" counties left to be districted!")
	ind = 1
print("multi county districts step 3 completed")
print(len(county_data))
print(" counties left to be districted!")
print(districts)



i = 0
while len(county_data) > 0:
	if i == len(county_data):
		i = 0
	county_to_district = county_data[i]
	counties_adjacent_to_this_one = get_adjacent_counties(county_to_district[0])
	non_districted_adjacent_counties = adjacent_counties[i]
	for j in range(0, len(counties_adjacent_to_this_one)):
		for k in range(0, len(non_districted_adjacent_counties)):
			if j < len(counties_adjacent_to_this_one) and k < len(non_districted_adjacent_counties):
				if counties_adjacent_to_this_one[j] == non_districted_adjacent_counties[k]:
					counties_adjacent_to_this_one.remove(counties_adjacent_to_this_one[j])
	rand_ceil = len(counties_adjacent_to_this_one)
	if rand_ceil > 0:
		random_index = np.random.randint(0, rand_ceil)
		buddy_county = counties_adjacent_to_this_one[random_index]
		district_index = get_multi_county_district_index(buddy_county)
		multi_county_districts[district_index].append(county_to_district)
		county_districted = county_to_district[0]
	i = i+1
	print(len(county_data))
	print(" counties left to be districted!")

print(multi_county_districts)
print(len(districts) + len(multi_county_districts))
num_counties = 4
for j in range(0, len(multi_county_districts)):
	dist = multi_county_districts[j]
	num_counties = num_counties + len(dist)
print("there are ")
print(num_counties)
print(" in georgia")
"""
