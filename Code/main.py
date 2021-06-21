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
    covariance_factor = 3 #nie szaleć (dobrac zakres tak zeby drona nie wyjebac poza mape)
    alg_iteration = 5
    max_drone_cost = 8
    min_cost = 1
    max_cost = 3
    drones_params = helper.generate_drones_params(graph_size, drones_amount, max_drone_cost, drones_clusters, covariance_factor)
    build_cost = helper.generate_build_cost(graph_size, min_cost, max_cost)
    
    i = 0
    average_cost = 0
    variance_list = []
    cost_list = []
    while i < 10:
        cost = ga.full_algorithm(drones_params, build_cost, pop_size, alg_iteration, graph_size, max_drones_in_station)
        i += 1
        average_cost += cost
        cost_list.append(cost)

    average_cost = average_cost/10
    variance_list = [(v-average_cost)**2 for v in cost_list]
    variance = sum(variance_list)/10
    std = np.sqrt(variance)

    print("Średni koszt dla 10 prób: ", average_cost)
    print("Wariancja dla 10 prób: ", variance)
    print("Odchylenie standardowe dla 10 prób: ", std)



def Wojtek_test():
    seed()
    graph_size = 256
    pop_size = 100
    drones_amount = 30
    max_drones_in_station = round(drones_amount * 0.2)
    drones_clusters = 128
    covariance_factor = 1  # nie szaleć (dobrac zakres tak zeby drona nie wyjebac poza mape)
    alg_iteration = 5
    max_drone_cost = 8
    min_cost = 1
    max_cost = 3
    drones_params = helper.generate_drones_params(graph_size, drones_amount, max_drone_cost, drones_clusters,
                                                  covariance_factor)
    build_cost = helper.generate_build_cost(graph_size, min_cost, max_cost)

    i = 0
    average_cost = 0
    variance_list = []
    cost_list = []
    while i < 10:
        cost = ga.full_algorithm(drones_params, build_cost, pop_size, alg_iteration, graph_size, max_drones_in_station)
        i += 1
        average_cost += cost
        cost_list.append(cost)

    average_cost = average_cost/10
    variance_list = [(v-average_cost)**2 for v in cost_list]
    variance = sum(variance_list)/10
    std = np.sqrt(variance)

    print("Średni koszt dla 10 prób: ", average_cost)
    print("Wariancja dla 10 prób: ", variance)
    print("Odchylenie standardowe dla 10 prób: ", std)



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

