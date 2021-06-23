from Code.genetic_algorithm import Individual, Drone

import matplotlib.pyplot as plt
from typing import List


def print_pop(pop, msg=""):
    print("\nPrinting POP ", msg)
    for i in pop:
        print(i)

    print("\n")


def visualisation(stations: List[Individual], drones_list: List[Drone], stations_radius: int, graph_size):
    stations_center_x = [i.chromosome[0] for i in stations]
    stations_center_y = [i.chromosome[1] for i in stations]
    drones_x = [d.x for d in drones_list]
    drones_y = [d.y for d in drones_list]

    fig, ax = plt.subplots()
    ax = plt.gca()
    ax.cla()
    ax.plot(graph_size, graph_size)
    for idx in range(len(stations)):
        circle = plt.Circle((stations_center_x[idx], stations_center_y[idx]), stations_radius, color='b', fill=False)
        ax.add_patch(circle)

    ax.plot(stations_center_x, stations_center_y, 'b.', markersize=40)
    ax.plot(drones_x, drones_y, 'kx', markersize=15)
    fig.set_size_inches(20, 20)
    fig.show()
