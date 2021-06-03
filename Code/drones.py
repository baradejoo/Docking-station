from typing import List, Tuple


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


class Individual:
    """Class containing individual chromosome and rating"""

    def __init__(self, station_coordinates_: List, prob_: float = 0):
        """
        :param chromosome: described one individual (station) as 2 coordinates in binary: x and y
        :param obj_fcn: cost function which it's minimise
        :param prob_: probability of choosing this individual
        """
        self.chromosome = station_coordinates_
        self.obj_fcn = 0
        self.prob = prob_

    def __str__(self) -> str:
        return f"Individual -> chromosome: {self.chromosome}, probability: {self.prob}, " \
               f"cost function: {self.obj_fcn}".format(self=self)
