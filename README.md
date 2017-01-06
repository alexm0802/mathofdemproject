# Math of Democracy Project

####Project Goals

* We want to make a map where districts are gerrymandered to ensure as close to proportional representation (PR) as possible
* This is a thought experiment in producing a new type of democracy that has some of the benefits of PR systems (i.e. proportional representation of political parties) and the benefits of plurality-majority systems (i.e. representatives remain accountable to home districts)
* We know that the efficiency gap will be very high
* Extremely gerrymandered districts also have some benefits: very red districts can choose between two Republican candidates and very blue districts can choose between two Democratic candidates (like WA district 7)

####Next Steps

* Alex is working on a function which will generate random districts
* Anna is working on a function that will score districts

####Internet Sources

* https://github.com/tonmcg/County_Level_Election_Results_12-16/blob/master/2016_US_County_Level_Presidential_Results.csv
  * Election results
* https://www.cs.plu.edu/courses/csci144/fall2016/assignments.php
  * County outline data
* http://autoredistrict.org/ 
  * Has a lot of information on how to do the project

####Algorithm

* Generate some random maps
* Pick the best map
* Mutate that map
* Pick the best out of mutated ones and repeat
* If we have time, we can also create a method that will combine the two best scoring ones

####Assumptions

* Consistent population distribution throughout counties (we broke up a few counties that were too big)
* We will use voting population for population (this was ruled constitutional by SCOTUS)
* Independent voters are insignificant and can be ignored for making proportional districts
* 2012 election results approximately represent the political party alignment of citizens. We added noise to the score to represent people changing, but the mean value of the normal distribution used was still 0

####Notes

* Using only voters to define the population will be simpler, even though it isn’t how the Georgia actually creates districts (but it is constitutional, so I think it’s fine if we do that. The teachers realize that we have a limited amount of time)


* Georgia is probably a good state choice because it has a lot of small counties and it has a lot of people


* Some counties might have too many people, so we might not get a very good result


* The swapping districts will be much more difficult than it looks


* This program currently looks super slow… We don’t need to do a ton of optimization, but it might be bad if it is so slow that we can’t run it effectively


* Ideally, we write the code so that after doing Georgia, we can do other states (but the above problem of too big counties will be even more problematic in California… Maybe we could do IA, TE, NC or something similar that might work similarly to Georgia, but not every state


####How to push to git

*Use git status to ensure everything is working properly*

1. git pull
2. git add *filename* (or . if you want to add all modified files)
3. git commit -m "commit message"
4. git push
