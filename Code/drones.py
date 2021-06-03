from typing import List, Tuple


class Drone:
    def __init__(self, id_, drone_param_: Tuple):
        self.id = id_
        self.x0 = x0
        self.y0 = y0


class Individual:
    """Class containing individual chromosome and rating"""

    def __init__(self, station_coordinates_: Tuple, prob_: float = 0):
        """
        :param chromosome: opisac to
        """

        self.chromosome = station_coordinates_
        self.obj_fcn = 0
        self.prob = prob_

    def __str__(self):
        return str(self.ch_t) + ' ' + str(self.ch_p) + ' ' + str(self.prob) + ' ' + str(self.obj_fcn) + ' ' + \
               str(len(self.ch_p))
