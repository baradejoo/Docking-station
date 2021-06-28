import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from typing import List
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
from PIL import Image


def print_pop(pop, msg=""):
    print("\nPrinting POP ", msg)
    for i in pop:
        print(i)

    print("\n")



def visualisation(stations: List, drones_list: List, stations_radius: int, graph_size, iteration_to_averaged: int):
    filename = "../drone.png"
    drone_img = Image.open(filename, 'r')
    fixed_height = 50
    height_percent = (fixed_height / float(drone_img.size[1]))
    width_size = int((float(drone_img.size[0]) * float(height_percent)))
    drone_img = drone_img.resize((width_size, fixed_height), Image.NEAREST)

    text_img = Image.new('RGBA', (49, 50), (0, 0, 0, 0))
    text_img.paste(drone_img, (0, 0), mask=drone_img)
    drone_box = OffsetImage(text_img, zoom=1)

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

    for idx in range(0, len(drones_x)):
        ab = AnnotationBbox(drone_box, (drones_x[idx], drones_y[idx]), frameon=False)
        ax.add_artist(ab)
    ax.plot(stations_center_x, stations_center_y, 'b.', markersize=40)
    ax.set_title("Iteracja nr {}".format(iteration_to_averaged), fontsize=50)
    ax.set_xlabel('współrzędna x', fontsize=30)
    ax.set_ylabel('współrzędna y', fontsize=30)
    # ax.plot(drones_x, drones_y, 'o')
    fig.set_size_inches(20, 20)
    fig.show()
