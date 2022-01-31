import copy
from math import inf
import grid, tour, random, mutate
from main import NUM_CITIES, POPULATION_SIZE, ELITE_SIZE, NUM_PARENTS

################################################################
#util.py
#This module hosts methods that will handle repetetive heavy lifting for the search algorithms
#the algorithms should be able to get all the outside data and functionality that they need 
#from util.py
#
#getTourCost():
#gets the total cost for a tour of the cities, the search algorithms use this value
#to determine an effective move and to find local maxima
#
###############################################################


#calculate the cost for this tour, return cost as an integer
#Change TourCost to receive a tour as a list (example lsit of [0-4] is [0,1,2,3,4])
#return cost as an integer

def initialize (city_tour, current_population, cost_map, worst_tours, best_tours, list_of_tours, WORST_SIZE):
    #city_tour is the grid object to pass to the genetic algorithms
    #setGrid is required to establish cost to travel from city to city
    #getRandomTour can be used to seed the initial generation    
    city_tour.setGrid()
    
    #populate initial generation
    seedFirstGeneration(POPULATION_SIZE, city_tour, current_population, cost_map, list_of_tours)

    #map tour cost to the tour object and sort by tour cost
    #util.mapTourList(current_population)
  
    #get best and worst tours for easy reference
    #best tours will reproduce, worst tours will be replaced
    getBestTours(ELITE_SIZE, best_tours, cost_map)
    getWorstTours(WORST_SIZE, worst_tours,cost_map)

#returns cost of a tour, tour cost is our fitness
def getTourCost(tour, cost_graph):
    cost = 0
    copy_of_tour = []
    for i in tour:
        copy_of_tour.append(i)
    #create list of coordinates for flight costs
    #add home city to end of tour list
    copy_of_tour.append(copy_of_tour[0])

    #build list of cost grid coordinate sets (represents the tour)
    tour_coordinates = []
    for i in range(len(copy_of_tour)):
        if i == len(copy_of_tour)-1:
            break
        tour_coordinates.append((copy_of_tour[i], copy_of_tour[i+1]))    

    for flight in tour_coordinates:
        this_flight_cost = cost_graph[flight[0]][flight[1]]
        cost += this_flight_cost

    copy_of_tour.clear()
    return cost


#seeds initial generation with a randomly generated population
#this should give us a wide range of initial memebers to choose from
def seedFirstGeneration(population_size, city_tour, current_population, cost_map, list_of_tours):
    
    while len(current_population) < population_size:
        x = tour.Tour()
        x.setGeneration(1)
        x.setTour(city_tour.getRandomTour())
        x.setCost(getTourCost(x.getTour(), city_tour.getGrid()))
        #ensure that we don't seed our first generation with replicas
        if (x.getCost() not in cost_map.keys()) and (x.getTour() not in list_of_tours):
            current_population.append(x)
            list_of_tours.append(x.getTour())
            cost_map[x.getCost()] = x

#maps tour cost to tour object for later assessment
#tour cost is esseentially our fitness
def mapTourList(current_population):
    temp_map = {}
    for tour in current_population:
        temp_map[tour.getCost()] = tour
    return temp_map

#returns a map of the best tours (cost mapped to tour object)
def getBestTours(num_tours, best_tours ,cost_map):
    for i, (j,k) in enumerate(sorted(cost_map.items())):
        if i >= num_tours: break
        best_tours.append(k)
    
#returns a map of worst tours
def getWorstTours(num_tours, worst_tours, cost_map):
    cost_values = sorted(cost_map.keys())
    for i in range (len(cost_values)-num_tours, len(cost_values)):
        worst_tours.append(cost_map[cost_values[i]])
    

#used for crossing over genes in gene crossover operator
def getCrossoverIndex(index, length):
    if index >= length-1:
        return 0
    return index+1

#calls breeding operators and selects the next generation
def getTournamentParents (curr_gen, how_many):    
    #select parents for tournament
    parents = []    
    for i in range(how_many): 
        #get 4 parents for each round of tournament
        candidate_parents = []
        for j in range(4):
            candidate_parent = curr_gen[random.randrange(0, POPULATION_SIZE)]
            while candidate_parent in candidate_parents:
                candidate_parent = curr_gen[random.randrange(0, POPULATION_SIZE)]
            candidate_parents.append(candidate_parent)
        lowest_cost = inf
        parent = None
        for candidate in candidate_parents:
            if candidate.getCost() < lowest_cost: parent, lowest_cost = candidate, candidate.getCost()
        while parent in parents:
            parent = curr_gen[random.randrange(0, POPULATION_SIZE)]
        parents.append(parent)
    return parents

#performs the crossover operator
def breedCrossover (parents):
    #first, perform crossover
    children = []
    for i in range(0, len(parents), 2):               
        child1, child2 = mutate.orderCrossover(parents[i], parents[i+1], NUM_CITIES)
        children.append(child1)
        children.append(child2)
    return children

#remove worst individuals from population
def getSacrifice(cost_map, current_population, worst_tours):
    for item in worst_tours:                    
            current_population.remove(item)
            del cost_map[item.getCost()]
    worst_tours.clear()


#fill and order this generation


#make tour objects out of our children
def setChildren(children, current_population, cost_map, city_tour, generation):
    for child in children:
        x = tour.Tour()
        x.setGeneration(generation)
        x.setTour(child)
        x.setCost(getTourCost(x.getTour(), city_tour.getGrid()))
        current_population.append(x)
        cost_map[x.getCost()] = x