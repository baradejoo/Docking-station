import visualisation as vs


def genetic_alg(drones_params, build_cost, pop_size, alg_iteration):
    """Implementation of genetic algorithm
    :return: best solution"""

    pop = init_pop(pop_size)
    pop, best_sol, best_val, av_sol = fitness(drones_params, build_cost, pop)
    pop = selection(drones_params, build_cost, pop)

    i = 1
    while i <= alg_iteration:
        pop = cross_pop()
        pop = mutation()
        pop, it_best_sol, it_best_val, av_sol = fitness()

        if it_best_sol.obj_fcn < best_sol.obj_fcn:
            best_sol = deepcopy(it_best_sol)

        pop = selection(data, pop)

        i += 1

    return best_sol, best_sol_vec, av_sol_vec


def init_pop(pop_size) -> List[Individual]:
    pass
    # TODO: losowanie wspolrzednych stacji
    # jeden osobnik to jedna stacja !!!


def fitness(build_cost, pop):
    pass
    # TODO: liczyc wartosci funckji celu dla kazdego osobnika i prawdopobienstwo wybrania na podsawie funkji ceku
    # TODO: prawdopobienstwo = funkcja celu jednego osobnika/  sume wszystkich


def selection(drones_params, build_cost, pop):
    pass
    # TODO: selekcja, kolo ruletki na podstawie wyliczonych prawdopobienstw z fitness


def cross_pop():
    pass
    # TODO: binarnie!!! polowa z pierwszego krzyzyuje sie z polowa z drugiego

def mutation():
    pass
    # TODO: binarni!! zamiana losowych bitow w jednym osobniku


