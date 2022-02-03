from math import inf
from os import remove
import grid, util, sys, tour, mutate


#################################################
#
#This program solves the Traveling Salesperson problem 
#using Genetic Algortihms
#
#################################################

#set this to  desired generations
NUM_GENERATIONS = 5000
#set this to the desired population size
POPULATION_SIZE = 50
#set this to the desired number of cities
NUM_CITIES = 25
#Number of elites to carry over and worsts to get rid of
ELITE_SIZE, WORST_SIZE = 10, 10
#set the number of parents to select for breeding
NUM_PARENTS = 10
#stores the current population of tour objects
current_population = []
#stores the tours for replica checking
list_of_tours = []
#maps trip cost to tour object
cost_map = {}
#stores the top x of the tours for reproduction
best_tours = []
#stores the worst x of the tours for replacement
worst_tours = []
#this is the cost grid that we will use for all 12 runs
city_tour = grid.Grid(NUM_CITIES)



def main():
    
    #initialize variables for tours and starting lowest cost
    best_insert_tour = None
    best_insert_cost = inf
    best_swap_tour = None
    best_swap_cost = inf
    best_inversion_tour = None
    best_inversion_cost = inf
    best_scramble_tour = None
    best_scramble_cost = inf
    user_input = None

    #seed first generation and get initial best/worst cost values
    util.initialize(city_tour, current_population, cost_map, worst_tours, best_tours, list_of_tours, WORST_SIZE)
    
    print("\nWelcome to the 'Traveling Salesperson' route finding application\n")


    for i in range (NUM_GENERATIONS):
        #TODO!!! ensure that the population doesn't converge into a bunch of replicas
      
        #select parents for tournament selection        
        parents = util.getTournamentParents(current_population, NUM_PARENTS)
        
        #perform crossover        
        children = util.breedCrossover(parents)
        
        #perform additional mutations
            #TODO: handle/call the four different operators here
        
        #select the worst individuals for removal
        
        util.getSacrifice(cost_map, current_population, list_of_tours, worst_tours)
       
        #randomly select additional individuals to kill
            #we will use this if we want to kill off additional tours
            #and make more children

        #fill and order this generation, make tour objects out of our children
        util.setChildren(children, current_population, cost_map, city_tour, list_of_tours, i+2)
               
       
        util.getWorstTours(WORST_SIZE, worst_tours, cost_map)
        util.getBestTours(1, best_tours, cost_map)
        
        if i % 100 == 0: print("The best currently is: ", best_tours[0].getCost(), " From generation: ", best_tours[0].getGeneration())
        best_tours.clear()

    print ("All done!")

if __name__=='__main__':
        main()