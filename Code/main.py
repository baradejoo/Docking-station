import test

def test_4_skupiska():
    # parameters for test 1:
    graph_size = 256
    pop_size = 300
    iteration_to_averaged = 10  # number of iteration needed to calculate mean and standard dev (variance also)
    gen_iteration = 5

    drones_amount = 100
    drones_clusters = 128
    max_drone_cost = 8
    covariance_factor = 3

    min_cost = 1
    max_cost = 5
    test.test(graph_size, pop_size, iteration_to_averaged, gen_iteration,
              (drones_amount, max_drone_cost, drones_clusters, covariance_factor),
              (min_cost, max_cost))


def test_1_skupisk():
    # parameters for test 1:
    graph_size = 256
    pop_size = 300
    iteration_to_averaged = 10  # number of iteration needed to calculate mean and standard dev (variance also)
    gen_iteration = 5

    drones_amount = 200
    drones_clusters = 256
    max_drone_cost = 8
    covariance_factor = 3

    min_cost = 1
    max_cost = 5
    test.test(graph_size, pop_size, iteration_to_averaged, gen_iteration,
              (drones_amount, max_drone_cost, drones_clusters, covariance_factor),
              (min_cost, max_cost))

def test_rozwalone_drony():
    graph_size = 256
    pop_size = 200
    iteration_to_averaged = 10  # number of iteration needed to calculate mean and standard dev (variance also)
    gen_iteration = 20

    drones_amount = 100
    drones_clusters = 32
    max_drone_cost = 8
    covariance_factor = 6

    min_cost = 1
    max_cost = 3
    test.test(graph_size, pop_size, iteration_to_averaged, gen_iteration,
              (drones_amount, max_drone_cost, drones_clusters, covariance_factor),
              (min_cost, max_cost))

if __name__ == '__main__':
    # parameters for test 1:
    #test_rozwalone_drony()
    test_1_skupisk()