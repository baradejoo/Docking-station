from random import randint
from typing import List, Tuple
import genetic_algorithm as ga


class Drone:
    """Class containing drone parameters"""

    def __init__(self, id_, drone_param_: Tuple):
        """
        :param id: id of each drone
        :param x_0: x coordinate of drone at the map
        :pamram y_0: y coordinate of drone at the map
        """
        self.id = id_
        self.x_0, self.y_0, self.income = drone_param_

    def __str__(self) -> str:
        return f"Drone no. {self.id} -> coordinates: [{self.x_0},{self.y_0}], income: " \
               f"{self.income}".format(self=self)


def generate_drones_params(graph_size, drones_amount, max_cost) -> List[Tuple]:
    drones_params = []
    for i in range(0, drones_amount):
        x_0 = randint(0, graph_size)
        y_0 = randint(0, graph_size)
        income = randint(1, max_cost)
        drone = (x_0, y_0, income)
        drones_params.append(drone)

    return drones_params


def generate_stations_localisation(pop_size, graph_size) -> List[Tuple[int]]:
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


def convert_chromosome_to_bin(ind, max_number_gens: int) -> str:
    max_bits = max_number_gens
    part1_gen = format(ind.chromosome[0], f'0{max_bits}b')
    part2_gen = format(ind.chromosome[1], f'0{max_bits}b')
    gen = part1_gen + part2_gen

    if len(gen) != (2 * max_bits):
        raise ga.Exception1

    return gen
