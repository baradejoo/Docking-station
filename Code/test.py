import genetic_algorithm as ga
import helper_functions as helper
import copy
import numpy as np
import matplotlib.pyplot as plt
from random import seed
from typing import Tuple


def test(graph_size, pop_size, iteration_to_averaged, gen_iteration, gen_drones_params: Tuple, gen_build_params: Tuple):
    seed()
    max_drones_in_station = round(gen_drones_params[0] * 0.2)
    all_iter_station_costs = np.zeros((iteration_to_averaged, pop_size))
    all_iter_average_cost = np.zeros((1,iteration_to_averaged))
    all_iter_average_num = copy.deepcopy(all_iter_average_cost)
    drones_params = helper.generate_drones_params(graph_size, *gen_drones_params)
    build_costs = helper.generate_build_cost(graph_size, *gen_build_params)

    i = 0
    while i < iteration_to_averaged:
        station_costs = ga.full_algorithm(graph_size, pop_size, gen_iteration, max_drones_in_station,
                                          drones_params, build_costs, i)
        sum_costs = np.sum(station_costs)
        all_iter_average_cost[0, i] = sum_costs
        all_iter_average_num[0, i] = len(station_costs)

        print("-------------------------- Final (the best) set no. {} --------------------------".format(i))
        print("Number of station: ", len(station_costs))
        print("Sum all cost function of Individuals (Stations): ", sum_costs)
        all_iter_station_costs[i, 0:len(station_costs)] = station_costs[:]
        i += 1

    min_needed_elem_row = 0
    for i in range(len(all_iter_station_costs)):
        if min_needed_elem_row < all_iter_station_costs[i].tolist().index(0):
            min_needed_elem_row = all_iter_station_costs[i].tolist().index(0)

    all_iter_station_costs = all_iter_station_costs[:, 0:min_needed_elem_row]
    mean_all_station_costs = np.mean(all_iter_station_costs, axis=0)
    std_all_station_costs = np.std(all_iter_station_costs, axis=0)
    var_all_station_costs = np.var(all_iter_station_costs, axis=0)
    mean_all_iter_average_costs = np.mean(all_iter_average_cost, axis=1)
    mean_all_iter_average_num = np.mean(all_iter_average_num, axis=1)
    std_all_iter_average_costs = np.std(all_iter_average_cost, axis=1)
    std_all_iter_average_num = np.std(all_iter_average_num, axis=1)

    print("\n--------------------------------- Final summary --------------------------------".format(i))
    # print("Mean of all iteration for each station: \n", mean_all_station_costs)
    # print("Standard deviation of all iteration for each station: \n", std_all_station_costs)
    # print("Variance of all iteration for each station: \n", var_all_station_costs)
    print("Mean of all iteration's costs: ", mean_all_iter_average_costs)
    print("Mean of all iteration's number of stations: ", mean_all_iter_average_num)
    print("Standard deviation of all iteration's costs: ", std_all_iter_average_costs)
    print("Standard deviation of all iteration's number of stations: ", std_all_iter_average_num)

    plt.errorbar(np.linspace(0, len(mean_all_station_costs) - 1, num=len(mean_all_station_costs)),
                 mean_all_station_costs, yerr=std_all_station_costs, fmt='.')
    plt.xticks(np.arange(0, len(mean_all_station_costs), 1.0))
    plt.title(
        "Mean and standard deviation for each station after {} iteration".format(iteration_to_averaged))
    plt.xlabel("Station")
    plt.ylabel("Cost function")
    plt.show()
