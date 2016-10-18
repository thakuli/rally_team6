import json
from dao.Data import Beacon
from dao.Data import Coordinate
from dao.Data import Compass


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
        print "baddr={}, rssi={}, time_to_go={}, command_id={}, compass={}".format(self.baddr, self.rssi,
                                                                                   self.time_to_go, self.command_id,
                                                                                   self.compass.to_string())


def read_json(json_data):
    return json.loads(json_data)


# testausta
def testi():
    test_data = '{"baddr" : "71:E9:F6:72:21:FB", "rssi" : "-72", "time_to_go" : "0", "command_id" : "255", "x" : "-90", "y" : "147", "z" : "-127"}'

    file = open('rally.txt', 'r')

    previous = -50
    previous1 = -50
    previous2 = -50
    for line in file:
        ri = ReadInfo(read_json(line))

        print float((float(ri.rssi) + float(previous) + float(previous1) + float(previous2)) / 4)

        previous2 = previous1
        previous1 = previous
        previous = ri.rssi


# main
if __name__ == "__main__":
    testi()
