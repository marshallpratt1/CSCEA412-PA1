Background: Consider the dilemma of Traveling Salespersons. Starting from their home city, their task is to visit every city on a specified tour exactly once and return to their home city, while minimizing the total cost of the tour. Cost can be measured in several ways (total time, total distance traveled, etc.), but for our purposes lets assume that our salespeople are trying to minimize the total travel budget expended on the tour. For your first CSCE A412 project, you and one or two teammates are required to develop a genetic algorithm (GA) that reads a list of current airfares for direct one-way flights between pairs of cities, and evolves a minimized-cost tour that solves the Traveling Salesperson Problem (TSP).

Airline ticket prices are hard to predict. For this problem, you should assume that the cost of a one-way ticket from city I to city J is a random integer value uniformly distributed between $99 and $2000. Note that your cost grid will be asymmetric: a flight from city I to city J will generally NOT equal the cost of a flight from J to I.

One difficulty in solving the TSP using a GA is that standard mutation and crossover operators almost always produce offspring that fail to complete the tour. Eiben and Smith (pp. 45-6, 52-57) describe several operators designed to work with permutations. For this project, you should implement Order Crossover (OX) and each of the mutation operators described in the notes: insert, swap, inversion, and scramble mutation. 

Collect the following data for this project:

1.	Run your GA 12 times (three times for each mutation operator). 
2.	Begin each run by using a specific random number seed to generate a particular cost grid. The same cost grid should be used for all 12 runs. Also note the values used for the population size (M) and the maximum number of generations (G), and record the probabilities of crossover (pc), mutation (pm), and reproduction (pr) for all 12 runs.
3.	All 12 runs will use OX.
4.	For the first three runs, use insert mutation. After creating the cost grid, re-seed your random number generator with a different value for each run, thus producing a different initial population of tours. After each generation, your GA should record the best-of-generation tour, as well as its fitness. At the end of the run, report the best-of-run solution, the generation in which the best-of-run solution was found, and the fitness of the best-of-run solution. 
5.	Repeat step 4 using swap mutation.
6.	Repeat step 4 using inversion mutation.
7.	Repeat step 4 using scramble mutation.

Each team should write a brief report that includes each of the following items:

1.	The name and preferred email address of each team member.
2.	A table representing the control parameters (M, G, pc, pm, pr), the type of mutation used, as well as the result (i.e., the best-of-run tour and its fitness value) from each of the 12 test runs. 
3.	A brief summary of the results of this programming assignment. Was your GA able to consistently find a high optimized solution? Did one mutation operator consistently outperform another (i.e., find a better tour, or find it in fewer generations)? 

Submit your report (only one submission per team) via email. I will return grades and comments to you via email.
