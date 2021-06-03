from typing import List, Tuple
import numpy as np
import matplotlib.pyplot as plt

stations_center_xy = [(100, 100), (56, 201), (56, 36), (134, 12)]
drones_xy = [(33, 33), (20, 20)]
stations_radius = [100, 50, 30, 20]

graph_size = 256


def visualisation(stations_center_coordinates: List[Tuple], drones_coordinates: List[Tuple], stations_radius: List):
    stations_center_x = [i[0] for i in stations_center_coordinates]
    stations_center_y = [i[1] for i in stations_center_coordinates]
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


visualisation(stations_center_xy, drones_xy, stations_radius)
