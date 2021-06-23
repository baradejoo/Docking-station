import test

if __name__ == '__main__':
    # parameters for test 1:
    graph_size = 256
    pop_size = 300
    iteration_to_averaged = 2  # number of iteration needed to calculate mean and standard dev (variance also)
    gen_iteration = 5

    drones_amount = 100
    drones_clusters = 128
    max_drone_cost = 8
    covariance_factor = 3

    min_cost = 1
    max_cost = 3

    test.test(graph_size, pop_size, iteration_to_averaged, gen_iteration,
              (drones_amount, max_drone_cost, drones_clusters, covariance_factor),
              (min_cost, max_cost))
