import numpy as np
import genetic_algorithm as ga
import helper_functions as helper
from random import seed



if __name__ == '__main__':
    seed()
    graph_size = 255
    pop_size = 10
    drones_amount = 40
    alg_iteration = 5
    max_drone_cost = 8
    min_cost = 1
    max_cost = 3
    drones_params = helper.generate_drones_params(graph_size, drones_amount, max_drone_cost)
    build_cost = helper.generate_build_cost(graph_size, min_cost, max_cost)
    ga.genetic_alg(drones_params, build_cost, pop_size, alg_iteration, graph_size)
