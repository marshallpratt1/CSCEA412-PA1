import copy

import grid, tour, random

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
def seedFirstGeneration(population_size, city_tour, current_population):
    for i in range (population_size):
        x = tour.Tour()
        x.setGeneration(1)
        x.setTour(city_tour.getRandomTour())
        x.setCost(getTourCost(x.getTour(), city_tour.getGrid()))
        current_population.append(x)

#maps tour cost to tour object for later assessment
#tour cost is esseentially our fitness
def mapTourList(current_population):
    temp_map = {}
    for tour in current_population:
        temp_map[tour.getCost()] = tour
    return temp_map

#returns a map of the best tours (cost mapped to tour object)
def getBestTours(num_tours, cost_map):
    best_tours = []
    for i, (j,k) in enumerate(sorted(cost_map.items())):
        if i >= num_tours: break
        best_tours.append(k)
    return best_tours

#returns a map of worst tours
def getWorstTours(num_tours, cost_map):
    worst_tours = []
    cost_values = sorted(cost_map.keys())
    for i in range (len(cost_values)-num_tours, len(cost_values)):
        worst_tours.append(cost_map[cost_values[i]])
    return worst_tours 

def getCrossoverIndex(index, length):
    if index >= length-1:
        return 0
    return index+1