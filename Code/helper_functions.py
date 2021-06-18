from random import randint
from typing import List, Tuple
import genetic_algorithm as ga
import numpy as np


def generate_drones_params(graph_size, drones_amount, max_cost, drones_clusters) -> List[Tuple]:
    divided_square_num = int(graph_size / drones_clusters * graph_size / drones_clusters)
    max_number_drones_in_square = drones_amount // divided_square_num
    left_number_drones_in_square = drones_amount - max_number_drones_in_square * divided_square_num
    # rand square with distributed drones position from: left_number_drones_in_square
    # lefts drones where distributed with number: max_number_drones_in_square in left squares
    drones_coordinates = []
    center_squares = []
    for i in range(0, int(np.sqrt(divided_square_num))):
        for j in range(0, int(np.sqrt(divided_square_num))):
            center = [drones_clusters * i + drones_clusters/2, drones_clusters * j + drones_clusters/2]
            center_squares.append(center)

    drones_coordinates_x = []
    drones_coordinates_y = []

    for i in range(0, len(center_squares)):
        print(i)
        x, y = np.random.multivariate_normal(center_squares[i], [[drones_clusters, 0], [0, drones_clusters]],
                                             max_number_drones_in_square).T
        for j in x:
            x = int(j)
            drones_coordinates_x.append(x)
        for j in y:
            y = int(j)
            drones_coordinates_y.append(y)

    # rand for left number of drones
    for i in range(left_number_drones_in_square):
        x = randint(0, graph_size)
        y = randint(0, graph_size)
        drones_coordinates_x.append(x)
        drones_coordinates_y.append(y)

    drones_params = []
    for i in range(len(drones_coordinates_x)):
        income = randint(1, max_cost)
        drone = (drones_coordinates_x[i], drones_coordinates_y[i], income)
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
    build_cost = [[0 for x in range(graph_size + 1)] for y in range(graph_size + 1)]
    for i in range(0, graph_size + 1):
        for j in range(0, graph_size + 1):
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


def convert_chromosome_to_BCD(ind, graph_size) -> List[str]:
    """
    :return: list with 2 strings, each of them described parts of chromosome (coordinates: x, y) in BCD code
    """
    number_BCD_parts = sum(c.isdigit() for c in str(graph_size))
    split_numbers_part1_gen = [int(i) for i in str(ind.chromosome[0])]
    split_numbers_part2_gen = [int(i) for i in str(ind.chromosome[1])]

    part1_gen = ""
    if len(split_numbers_part1_gen) < number_BCD_parts:
        added_BCD_parts = number_BCD_parts - len(split_numbers_part1_gen)
        for i in range(added_BCD_parts):
            part1_gen += "0000"

    for i in split_numbers_part1_gen:
        part1_gen += format(i, f'0{4}b')

    part2_gen = ""
    if len(split_numbers_part2_gen) < number_BCD_parts:
        added_BCD_parts = number_BCD_parts - len(split_numbers_part2_gen)
        for i in range(added_BCD_parts):
            part2_gen += "0000"

    for i in split_numbers_part2_gen:
        part2_gen += format(i, f'0{4}b')

    return [part1_gen, part2_gen]


def convert_BCD_to_decimal_chromosome(ind, graph_size) -> List[int]:
    """
    :return: list with 2 ints, each of them described parts of chromosome (coordinates: x, y) in decimal
    """
    print(ind)
    number_BCD_parts = sum(c.isdigit() for c in str(graph_size))
    decimal_list = []
    for i in ind:
        number = ""
        for j in range(number_BCD_parts):
            start = j * 4
            end = (j + 1) * 4
            divider = i[start:end]
            if divider != "0000":
                divider_int = int(divider, 2)
                if divider_int < 10:
                    number += str(divider_int)
                else:
                    number += str(randint(0, 9))
        decimal_list.append(int(number))

    print(decimal_list)

    return decimal_list
