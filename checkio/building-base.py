class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.start_point = [south, west]
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):
        corners = {"north-west": [self.start_point[0]+self.width_NS,
                                  self.start_point[1]],
                   "north-east": [self.start_point[0]+self.width_NS,
                                  self.start_point[1]+self.width_WE],
                   "south-west": self.start_point,
                   "south-east": [self.start_point[0],
                                  self.start_point[1]+self.width_WE]
                   }
        return corners

    def area(self):
        return self.width_WE * self.width_NS

    def volume(self):
        return self.area() * self.height

    def __repr__(self):
        return f"{self.__class__.__name__}({self.start_point[0]}, {self.start_point[1]}, {self.width_WE}, " \
               f"{self.width_NS}, {self.height})"
