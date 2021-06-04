from genetic_algorithm import Individual
from typing import List, Tuple
import numpy as np
import matplotlib.pyplot as plt


def visualisation(stations: List[Individual], drones_coordinates: List[Tuple], stations_radius: List):
    stations_center_x = [i.chromosome[0] for i in stations]
    stations_center_y = [i.chromosome[1] for i in stations]
    drones_x = [i[0] for i in drones_coordinates]
    drones_y = [i[1] for i in drones_coordinates]

    fig, ax = plt.subplots()
    ax = plt.gca()
    ax.cla()
    fig.set_size_inches(15, 15)
    ax.plot(graph_size, graph_size)
    for idx, val in enumerate(stations_radius):
        circle = plt.Circle((stations_center_x[idx], stations_center_y[idx]), val, color='b', fill=False)
        ax.add_patch(circle)

    ax.plot(stations_center_x, stations_center_y, 'bx', drones_x, drones_y, 'ko')
    fig.show()
