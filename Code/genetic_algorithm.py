import visualisation as vs
import drones
import numpy as np
from typing import List, Tuple
from random import randint


class Exception1(Exception):
    def __init__(self, message="Something goes wrong! -> Two different sizes"):
        self.message = message
        super().__init__(self.message)


def genetic_alg(drones_params, build_cost, pop_size, alg_iteration, graph_size):
    """Implementation of genetic algorithm
    :return: best solution"""

    drones_list = []  # Containing list of drones objects

    # Creating drones objects
    for idx, params in enumerate(drones_params):
        drones_list.append(drones.Drone(idx, params))

    pop = init_pop(pop_size, graph_size)
    print(pop[5])
    # pop, best_sol, best_val, av_sol = fitness(drones_params, build_cost, pop)
    # pop = selection(drones_params, build_cost, pop)

    # i = 1
    # while i <= alg_iteration:
    #     pop = cross_pop()
    #     pop = mutation()
    #     pop, it_best_sol, it_best_val, av_sol = fitness()
    #
    #     if it_best_sol.obj_fcn < best_sol.obj_fcn:
    #         best_sol = deepcopy(it_best_sol)
    #
    #     pop = selection(data, pop)

        # i += 1

    return 1

# TODO: do przerzucenia do pliku z funkjami pomocniczymi
def generate_drones_params(graph_size, drones_amount, max_cost) -> List[Tuple]:
    drones_params = []
    for i in range(0, drones_amount):
        x_0 = randint(0, graph_size)
        y_0 = randint(0, graph_size)
        income = randint(1, max_cost)
        drone = (x_0, y_0, income)
        drones_params.append(drone)
    return drones_params


def generate_stations_localisation(pop_size, graph_size) -> List[Tuple]:
    stations_coordinates = []
    for i in range(0, pop_size):
        x = randint(0, graph_size)
        y = randint(0, graph_size)
        coordinates = (x, y)
        stations_coordinates.append(coordinates)

    return stations_coordinates

def generate_build_cost(graph_size, min_cost, max_cost):
    build_cost = [[0 for x in range(graph_size)] for y in range(graph_size)]
    for i in range(0, graph_size):
        for j in range(0, graph_size):
            build_cost[i][j] = randint(min_cost, max_cost)
    return build_cost

def init_pop(pop_size, graph_size) -> List[drones.Individual]:
    """ Function witch initializes population and returns it as a list of Individuals """

    population = []
    stations_coordinates = generate_stations_localisation(pop_size, graph_size)

    if len(stations_coordinates) == pop_size:
        for i in range(0, pop_size):
            population.append(drones.Individual(i, stations_coordinates[i]))
    else:
        raise Exception1

    return population


def fitness(build_cost, pop):
    pass
    # TODO: liczyc wartosci funckji celu dla kazdego osobnika i prawdopobienstwo wybrania na podsawie funkji ceku
    # TODO: prawdopobienstwo = funkcja celu jednego osobnika/  sume wszystkich


def selection(drones_params, build_cost, pop: List[Individual]):
    """Select individuals based on probability calculated by fitness
        :return: population to reproduce"""

    new_pop = []
    while len(new_pop) < len(pop):
        r = random.random()
        prob = 0
        for i in pop:
            prob += i.prob
            if prob > r:
                new_pop.append(i)
                break
    return new_pop

def cross_pop():
    pass
    # TODO: binarnie!!! polowa z pierwszego krzyzyuje sie z polowa z drugiego

def mutation():
    """Mutates random gens with probability
        :return: population with small percentage of mutated individuals"""
    # TODO: binarni!! zamiana losowych bitow w jednym osobniku


