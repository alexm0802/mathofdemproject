#Currently, there isn't really a way to test this code, so there could be a lot
#of errors...
#also, we are using dem+rep, instead of total to ignore idependent voters (but add extra noise)
#for the sake of the statistical stuff
import numpy as np
def prob (county_totals, county_probs): #adding arbitrary amount of noise, maybe calculate specific later
#by calculating standard deviation of change from 2012 to 2016 or something
    sdev = np.random.normal(0, .05, len(county_probs)).tolist()
    dist_probs = [sum(x) for x in zip(county_probs, sdev)]
    return sum([a*b for a,b in zip(dist_probs,county_totals)])

def calc_score (n_map, county_data):
    ideal_breakdown = sum(county_data[:,2])/(sum(county_data[:,2])+sum(county_data[:,3]))
    score
    for i in n_map:
        county_totals
        county_probs
        for j in n_map[i]:
            index = county_data.index(n_map[i:j])
            county_totals.append(county_data[index:2] + county_data[index:3])
            county_probs.append(county_data[index:2]/(county_data[index:2] + county_data[index:3]))
        score += prob(county_totals, county_probs)/14
    return score
