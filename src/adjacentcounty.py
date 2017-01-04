#name of file containing data to read in
filename = "data/georgia_county_locations.txt"
is_valid = False
#check if (hardcoded) pathname is valid, if not prompts user to try again until they come up with a valid pathname
while is_valid != True:
	try:
		fi = open(filename)
		file_input = fi.read()
		is_valid = True
		print("Processing...")
	except:
		print("Filename invalid. Try again.")
		filename = input("What file containing counties would you like to use?  ")

#checks if a string is a number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
#sets up x-coordinates for counties and y-coordinates for counties
county_names = []
county_xcoord = []
county_ycoord = []
adjacent_counties = []
data = file_input.split()
for i in range(0, len(data)):
	if is_number(data[i])==False:
		if data[i]!='GA':
			county_names.append(data[i])
			if i+6 < len(data):
				j = i + 6
				k = j
				x_coord = []
				y_coord = []
				while k < len(data) and is_number(data[k])==True:
					if (k-j)%2==0:
						x_coord.append(data[k])
					if(k-j)%2==1:
						y_coord.append(data[k])
					k=k+1
				county_xcoord.append(x_coord)
				county_ycoord.append(y_coord)
#print(county_names)
#print(county_xcoord[0])
#print(county_ycoord)
for i in range(0, len(county_names)):
	x_list = county_xcoord[i]
	y_list = county_ycoord[i]
	adj_counties_outer = []
	for j in range(0, len(county_names)):
		x_list_comp = county_xcoord[j]
		y_list_comp = county_ycoord[j]
		num = 0
		for k in range(0, len(x_list)):
			x = x_list[k]
			y = y_list[k]
			for l in range(0, len(x_list_comp)):
				x_comp = x_list_comp[l]
				y_comp = y_list_comp[l]
				if x == x_comp:
					if y == y_comp:
						#print(county_names[i] + " and " + county_names[j] + " share an x at " + x + " and a y at " + y_list[k])
						num = num + 1
		if num > 1 and i != j:
			adj_counties_outer.append(county_names[j])
			print("appending " + county_names[j] + " to " + county_names[i])
	adjacent_counties.append(adj_counties_outer)


def are_these_counties_adjacent(county1, county2):
	index_of_county_1 = -1
	index_of_county_2 = -1
	for i in range(0, len(county_names)):
		if county_names[i] == county1:
			index_of_county_1 = i
	for i in range(0, len(county_names)):
		if county_names[i] == county2:
			index_of_county_2 = i
	if index_of_county_1 == -1 or index_of_county_2 == -1:
		print("one or more county names invalid. try again")
		return
	else:
		adj_counties = adjacent_counties[index_of_county_1]
		for i in range(0, len(adj_counties)):
			if adj_counties[i] == county2:
				return True
		return False

print(are_these_counties_adjacent("Appling", "JeffDavis"))
print(are_these_counties_adjacent("Appling", "Houston"))
print(are_these_counties_adjacent("Appling", "apples"))
print(are_these_counties_adjacent("apples", "Appling"))
print("done")
