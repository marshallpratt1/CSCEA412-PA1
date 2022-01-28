from math import cos, inf
import grid, util, sys, tour, mutate


#################################################
#
#This program solves the Traveling Salesperson problem 
#using Genetic Algortihms
#
#################################################

#set this to  desired generations
MAX_GENERATIONS = 100
#set this to the desired population size
MAX_POPULATION = 10
#set this to the desired number of cities
NUM_CITIES = 9
#stores the current population of tours
current_population = []
#maps trip cost to tour object
cost_map = {}
#stores the top x of the tours for reproduction
best_tours = []
#stores the worst x of the tours for replacement
worst_tours = []
#this is the cost grid that we will use for all 12 runs
city_tour = grid.Grid(NUM_CITIES)

def initialize ():
    #city_tour is the grid object to pass to the genetic algorithms
    #setGrid is required to establish cost to travel from city to city
    #getRandomTour can be used to seed the initial generation
    
    city_tour.setGrid()
    
    #populate initial generation
    util.seedFirstGeneration(MAX_POPULATION, city_tour, current_population)

    #map tour cost to the tour object and sort by tour cost
    cost_map = util.mapTourList(current_population)
  
    #get best and worst tours for easy reference
    #best tours will reproduce, worst tours will be replaced
    best_tours = util.getBestTours(2, cost_map)
    worst_tours= util.getWorstTours(2, cost_map)
    return cost_map, best_tours, worst_tours

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
    cost_map, best_tours, worst_tours = initialize()
  

    #below print statements are for debugging purposes only
    print("\nAll tours:")
    for i in sorted(cost_map.keys()):
        print (i, cost_map[i])
    print("\nBest tours:")
    for i in best_tours:
        print (i.getCost(), i)
    print("\nWorst tours:")
    for i in worst_tours:
        print (i.getCost(), i)
    print()
    for tour in best_tours:
        pass
    for i in range (1):
        first, second = mutate.orderCrossover(best_tours[0], best_tours[1], NUM_CITIES)
        print("First point: ", first, ", second point: ", second)
       

  


    print("\nWelcome to the 'Traveling Salesperson' route finding application\n")

    #run this until user chooses to exit
    while True:            

        city_tour.displayGrid()

        #Exit protocol, if user is finished then sys.exit()
        user_input = input("Would you like to run the program again?, Enter 'Y' to continue or any other key to exit: ")
        if user_input is not 'Y' and user_input is not 'y': sys.exit()
        else:
            #reset the best variables
            best_insert_tour = []
            best_insert_cost = inf
            best_swap_tour = []
            best_swap_cost = inf
            best_inversion_tour = []
            best_inversion_cost = inf
            best_scramble_tour = []
            best_scramble_cost = inf

if __name__=='__main__':
        main()