"""
initiate everything, and create arrays of counties, population, and %rep
deal with the counties that are super big, and create a few districts...
create 5 random district combinations, and calculate scores for them
combine best 2 district combinations into 1 map
mutate that map into 5 ones, and repeat previous three steps

issues:
creating the random maps: making sure population matches
combining maps
calculating scores (whatever we choose for this to mean)
"""
#a map will be  ____ = [14][] (or possibly shorter if separating large counties)
"""
def random_map (county_data):

def comb_map (map1, map2):

def calc_score (map):"""

def main ():
    f = open('data/georgia_2012_results.csv', 'r')
    f.readline()
    county_data = [] #county_data[0]=names, county_data[1]=total votes
                    #county_data[2]=rep votes, county_data[4]= dem votes
    for line in f:
        temp = line.split(',')
        county_data.append([temp[2], temp[7], temp[4], temp[5]])
    maps = []
    scores = []
    for i in range(0, 10):
        maps.append(random_map(county_data))
    for j in maps:
        scores.append(calc_score(maps[j]))
    while (True):


if __name__ == "__main__": main()
