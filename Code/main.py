import numpy as np
import genetic_algorithm as ga


if __name__ == '__main__':
    graph_size = 256
    pop_size = 30
    alg_iteration = 30
    drones_params = [(2,3,4), (3,4,4)]  # x,y,cost in tuple #TODO: wojtek
    build_cost = np.zeros(graph_size)  # TODO: wojtek, funckja ktora to robi    fun(cost_min, cost_max)

    ga.genetic_alg(drones_params, build_cost, pop_size, alg_iteration)
