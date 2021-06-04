import visualisation as vs
import helper_functions as helper
import numpy as np
from typing import List, Tuple
from random import randint, random
import random
import math


class Individual:
    """Class containing individual chromosome and rating"""

    def __init__(self, station_coordinates_: List, prob_: float = 0):
        """
        :param chromosome: described one individual (station) as 2 coordinates in binary: x and y
        :param obj_fcn: cost function which it's minimise
        :param prob_: probability of choosing this individual
        """
        self.chromosome = station_coordinates_
        self.obj_fcn = 0
        self.prob = prob_

    def __str__(self) -> str:
        return f"Individual -> chromosome: {self.chromosome}, probability: {self.prob}, " \
               f"cost function: {self.obj_fcn}".format(self=self)


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
        drones_list.append(helper.Drone(idx, params))

    pop = init_pop(pop_size, graph_size)

    crossover(pop[1], pop[2], graph_size)
    # new_pop = cross_pop(pop, graph_size, 0.5)
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


def init_pop(pop_size, graph_size) -> List[Individual]:
    """ Function witch initializes population and returns it as a list of Individuals """

    population = []
    stations_coordinates = helper.generate_stations_localisation(pop_size, graph_size)

    if len(stations_coordinates) == pop_size:
        for i in range(0, pop_size):
            population.append(Individual(stations_coordinates[i], 0))
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


def cross_pop(pop: List[Individual], graph_size, cross_factor) -> List[Individual]:
    """Crossing children with old population
        :return: new population"""

    crossed_pop = []
    i = 0
    while i < len(pop) * cross_factor :
        children = crossover(pop[i], pop[i+1], graph_size)
        crossed_pop.append(children[0])
        crossed_pop.append(children[1])
        i += 2
    while len(crossed_pop) < len(pop):
        r = random.random()
        prob = 0
        for e in pop:
            prob += e.prob
            if prob < r:
                crossed_pop.append(e)
                break
    return crossed_pop


def mutation(pop: List[Individual], mutation_factor: float, pop_size, graph_size) -> List[Individual]:
    """Mutates random gens with probability
        :return: population with small percentage of mutated individuals"""

    random_stations = []
    duplications = []
    mutated_amount = len(pop) * mutation_factor
    while len(random_stations) < mutated_amount:
        for i in range(int(mutated_amount)):
            x = randint(0, len(pop)-1)
            if x not in duplications:
                random_stations.append(x)
                duplications.append(x)
            if len(random_stations) == mutated_amount:
                break
    # print(random_stations)
    for e in random_stations:
        array_string = []
        # print(pop[e])
        string = helper.convert_chromosome_to_bin(pop[e], len(bin(graph_size)[2:]))
        # print("stary:", string, "\n")
        x = randint(0, len(string)-1)
        for i in string:
            array_string.append(int(i))
        if array_string[x] == 1:
            array_string[x] = 0
        else:
            array_string[x] = 1
        gen_x = array_string[:8]
        gen_y = array_string[8:]
        string_x = [str(int) for int in gen_x]
        string_x = "".join(string_x)
        string_y = [str(int) for int in gen_y]
        string_y = "".join(string_y)
        # print("nowy:", array_string, "\n")
        # print("genx:", gen_x, "\n", "geny:", gen_y,"\n")
        # print("string_x:", string_x)
        # print("string_y:", string_y)
        pop[e].chromosome = [int(string_x, 2), int(string_y, 2)]
        # print("chromosom:", pop[e].chromosome)


def method1_crossover(ind1: Individual, ind2: Individual, graph_size) -> Tuple[Individual, Individual]:
    max_number_gens = graph_size.bit_length()
    # print("Values: x and y before crossover fun.: {}, {} -> 1 parent".format(ind1.chromosome[0], ind1.chromosome[1]))
    # print("Values: x and y before crossover fun.: {}, {} -> 2 parent".format(ind2.chromosome[0], ind2.chromosome[1]))

    ind1_chromosome_bits = helper.convert_chromosome_to_bin(ind1, max_number_gens)
    ind2_chromosome_bits = helper.convert_chromosome_to_bin(ind2, max_number_gens)

    child1_chromosome_bits = ind1_chromosome_bits[:max_number_gens] + ind2_chromosome_bits[max_number_gens:]
    child2_chromosome_bits = ind2_chromosome_bits[:max_number_gens] + ind1_chromosome_bits[max_number_gens:]

    children = (Individual([int(child1_chromosome_bits[:max_number_gens], 2),
                            int(child1_chromosome_bits[max_number_gens:], 2)]),
                Individual([int(child2_chromosome_bits[:max_number_gens], 2),
                            int(child2_chromosome_bits[max_number_gens:], 2)]))

    # print("Values: x and y after crossover fun.: {}, {} -> 1 child".format(children[0].chromosome[0],
    #                                                                        children[0].chromosome[1]))
    # print("Values: x and y after crossover fun.: {}, {} -> 2 child".format(children[1].chromosome[0],
    #                                                                        children[1].chromosome[1]))

    return children


def method2_crossover(ind1: Individual, ind2: Individual, graph_size) -> Tuple[Individual, Individual]:
    """ Crossover function, which used BCD code to describe coordinates. It allows crossing gens in specific way,
        such as: crossing gens which described only number of units (not number od decimals or hundredths) """

    print("Values: x and y before crossover fun.: {}, {} -> 1 parent".format(ind1.chromosome[0], ind1.chromosome[1]))
    print("Values: x and y before crossover fun.: {}, {} -> 2 parent".format(ind2.chromosome[0], ind2.chromosome[1]))

    ind1_BCD = helper.convert_chromosome_to_BCD(ind1, graph_size)
    ind2_BCD = helper.convert_chromosome_to_BCD(ind2, graph_size)

    print(ind1_BCD)
    print(ind2_BCD)
    ind1_units_BCD = (ind1_BCD[0][-4:], ind1_BCD[1][-4:])
    ind2_units_BCD = (ind2_BCD[0][-4:], ind2_BCD[1][-4:])

    child1_chromosome_bits = [ind1_BCD[0][:-4] + ind1_units_BCD[0][:2] + ind2_units_BCD[1][-2:],
                              ind1_BCD[1][:-4] + ind1_units_BCD[0][-2:] + ind2_units_BCD[1][:2]]
    child2_chromosome_bits = [ind2_BCD[0][:-4] + ind1_units_BCD[1][:2] + ind2_units_BCD[0][-2:],
                              ind2_BCD[1][:-4] + ind1_units_BCD[1][-2:] + ind2_units_BCD[0][:2]]

    ind1_decimal = helper.convert_BCD_to_decimal_chromosome(child1_chromosome_bits, graph_size)
    ind2_decimal = helper.convert_BCD_to_decimal_chromosome(child2_chromosome_bits, graph_size)

    children = (Individual(ind1_decimal), Individual(ind2_decimal))

    print("Values: x and y after crossover fun.: {}, {} -> 1 child".format(children[0].chromosome[0],
                                                                           children[0].chromosome[1]))
    print("Values: x and y after crossover fun.: {}, {} -> 2 child".format(children[1].chromosome[0],
                                                                           children[1].chromosome[1]))

    return children



def crossover(ind1: Individual, ind2: Individual, graph_size) -> Tuple[Individual, Individual]:
    """ Crossing one part of individual with the other part of individual """
    """
       :param ind1: one of the parents who will be crossing with the other parent
       :param ind2: second one of the parents
       :return: children (new individual who is the part of the new population)
    """
    method = 2
    if method == 2:
        children = method2_crossover(ind1, ind2, graph_size)
    else:
        children = method1_crossover(ind1, ind2, graph_size)

    return children

