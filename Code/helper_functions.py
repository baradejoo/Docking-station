from random import randint
from typing import List, Tuple
import genetic_algorithm as ga



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
