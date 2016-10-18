import json
from dao.Data import Beacon
from dao.Data import Coordinate
from dao.Data import Compass

<<<<<<< HEAD
=======

class Compass:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def to_string(self):
        "x={}, y={}, z={}".format(self.x, self.y, self.z)
>>>>>>> b7ac9d5fe1906c68a84fb4ab63985723968400c3


class ReadInfo:

    def __init__(self, json):
        self.set_data(json)

    def set_data(self, json_data):
        self.baddr = json_data['baddr']
        self.rssi = json_data['rssi']
        self.time_to_go = json_data['time_to_go']
        self.command_id = json_data['command_id']
        self.compass = Compass(json_data['x'], json_data['y'], json_data['y'])

    def to_string(self):
        print "baddr={}, rssi={}, time_to_go={}, command_id={}, compass={}".format(self.baddr, self.rssi, self.time_to_go, self.command_id, self.compass.to_string())


def read_json(json_data):
    return json.loads(json_data)


# testausta
def testi():
<<<<<<< HEAD
    test_data='{"baddr" : "71:E9:F6:72:21:FB", "rssi" : "-72", "time_to_go" : "0", "command_id" : "255", "x" : "-90", "y" : "147", "z" : "-127"}'
    	
    ri = ReadInfo(read_json(test_data))
    ri.to_string()

    
=======
    test_data = '{"baddr" : "71:E9:F6:72:21:FB", "rssi" : "-72", "time_to_go" : "0", "command_id" : "255", "x" : "-90", "y" : "147", "z" : "-127"}'

    jsonD = json.loads(test_data)

    ri = ReadInfo()
    ri.set_data(jsonD)

    print "baddr={}, rssi={}, time_to_go={}, command_id={}, compass={}".format(ri.baddr, ri.rssi, ri.time_to_go,
                                                                               ri.command_id, ri.compass.to_string())

>>>>>>> b7ac9d5fe1906c68a84fb4ab63985723968400c3

# main
if __name__ == "__main__":
    testi()

