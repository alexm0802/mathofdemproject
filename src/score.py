#Currently, there isn't really a way to test this code, so there could be a lot
#of errors...
#also, we are using dem+rep, instead of total to ignore idependent voters (but add extra noise)
#for the sake of the statistical stuff
import numpy as np
def prob (count_totals, count_probs): #adding arbitrary amount of noise, maybe calculate specific later
#by calculating standard deviation of change from 2012 to 2016 or something
    sdev = np.random.normal(0, .05, len(dist_totals)).tolist()
    dist_probs = [sum(x) for x in zip(count_probs, sdev)]
    return sum([a*b for a,b in zip(dist_probs,count_totals)])

def calc_score (n_map, county_data):
    ideal_breakdown = sum(county_data[:,2])/(sum(county_data[:,2])+sum(county_data[:,3]))
    score
    for i in n_map:
        count_totals
        county_probs
        for j in n_map[i]:
            index = county_data.index(n_map[i:j])
            count_totals.append(county_data[index:2] + county_data[index:3])
            count_probs.append(county_data[index:2]/(county_data[index:2] + county_data[index:3]))
        score += prob(count_totals, count_probs)/14
    return score
