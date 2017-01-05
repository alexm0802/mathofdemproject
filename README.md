# Math of Democracy Project

####Project Goals

* We want to make a map where districts are gerrymandered to ensure as close to proportional representation (PR) as possible
* This is a thought experiment in producing a new type of democracy that has the same benefits as PR systems (i.e. proportional representation of political parties) and the same benefits of plurality-majority systems (i.e. representatives remain accountable to home districts)
* We know that the efficiency gap will be very high
* Extremely gerrymandered districts also have some benefits: very red districts can choose between two Republican candidates and very blue districts can choose between two Democratic candidates (like WA district 7)
  
####Next Steps

* Alex is working on a function which will generate random districts
* Anna is working on a function that will score districts
  * http://autoredistrict.org/ has some interesting information on how to make our code not suck (basically how to go about finding the best districts

####Internet Stuff

* Maybe just use the Georgia data from the 2016 Presidential Election (but some counties are so fucking big!!!)
  * https://github.com/tonmcg/County_Level_Election_Results_12-16/blob/master/2016_US_County_Level_Presidential_Results.csv
* https://www.cs.plu.edu/courses/csci144/fall2016/labs/lab07/lab07.pdf would make it possible to fill in the counties if we can find the correct code (maybe here https://www.cs.plu.edu/courses/csci144/fall2016/assignments.php)
  * Actually, with the county data file we don't need to use PLU's code, we can just do it in python. I'll work on that file
* If all of the above components work, we could create another file which contains information on which counties border, so when we create different districts, we can ensure that they are continuous by making sure every county borders at least one other county

####Pseudo-psuedo code assuming all of the above works

* Start with a county, iterate through and add other counties until we reach the threshold (make the threshold the average number of people per legislative district)


* Iterate through moving small districts until populations are similar enough


* Some sort of method that will swap districts of similar sizes (can be groupings of districts as well) and create a better political fairness value (or whatever that value was called)


* Repeat this step until no more switches are possible

####Notes

* Using only voters to define the population will be simpler, even though it isn’t how the Georgia actually creates districts (but it is constitutional, so I think it’s fine if we do that. The teachers realize that we have a limited amount of time)


* Georgia is probably a good state choice because it has a lot of small counties and it has a lot of people


* Assuming consistent population distribution throughout counties


* Some counties might have too many people, so we might not get a very good result BIG ISSUE ACTUALLY... Maybe premake some districts


* Finding the code to create the map correctly could be challenging


* The swapping districts will be much more difficult than it looks


* This program currently looks super slow… We don’t need to do a ton of optimization, but it might be bad if it is so slow that we can’t run it effectively


* Ideally, we write the code so that after doing Georgia, we can do other states (but the above problem of too big counties will be even more problematic in California… Maybe we could do IA, TE, NC or something similar that might work similarly to Georgia, but not every state


* Dividing the work on this project will be challenging. We will need to use Github, and also work at different times

####How to push to git

*Use git status to ensure everything is working properly*

1. git pull
2. git add *filename* (or . if you want to add all modified files)
3. git commit -m "commit message"
4. git push
