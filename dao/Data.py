class Beacon:
    def __init__(self, baddr, rssi):
        self.baddr = baddr
        self.rssi = rssi

class Coordinate:
    def __init__(self, beacon1, beacon2, beacon3):
        self.beacon1 = beacon1
        self.beacon2 = beacon2        
        self.beacon3 = beacon3


class Compass:
    def __init__(self, x, y , z):
        self.x = x
        self.y = y
        self.z = z
        
    def to_string(self):
        return "x={}, y={}, z={}".format(self.x, self.y, self.z)
