class Drone:
    class Operation:
        def __init__(self, c, m):
            self.c = c
            self.m = m
    def __init__(self, id, c, m, x, y, r):
        self.id = id
        self.x0 = x0
        self.y0 = y0
        self.r = r
        self.c = Drone.Operation(c)
        self.m = Drone.Operation(m)

class Operation:
    def __init__(self, c, m):
        self.c = c
        self.m = m


