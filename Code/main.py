import numpy as np
import genetic_algorithm as ga
import helper_functions as helper
from random import seed


def do_test():
    seed()
    graph_size = 256
    pop_size = 300
    drones_amount = 100
    max_drones_in_station = round(drones_amount * 0.2)
    drones_clusters = 128
    alg_iteration = 5
    max_drone_cost = 8
    min_cost = 1
    max_cost = 3
    drones_params = helper.generate_drones_params(graph_size, drones_amount, max_drone_cost, drones_clusters)
    build_cost = helper.generate_build_cost(graph_size, min_cost, max_cost)
    
    i = 0
    while i < 10:
        ga.full_algorithm(drones_params, build_cost, pop_size, alg_iteration, graph_size, max_drones_in_station)
        i += 1



if __name__ == '__main__':
    # seed()
    # graph_size = 255
    # pop_size = 10
    # drones_amount = 40
    # max_drones_in_station = round(drones_amount * 0.2)
    # alg_iteration = 5
    # max_drone_cost = 8
    # min_cost = 1
    # max_cost = 3
    # drones_params = helper.generate_drones_params(graph_size, drones_amount, max_drone_cost)
    # build_cost = helper.generate_build_cost(graph_size, min_cost, max_cost)
    #
    # ga.full_algorithm(drones_params, build_cost, pop_size, alg_iteration, graph_size, max_drones_in_station)

    do_test()

