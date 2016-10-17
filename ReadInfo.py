
import json

class Compass:
    def __init__(self, x, y , z):
        self.x = x
        self.y = y
        self.z = z
        
    def to_string(self):
        "x={}, y={}, z={}".format(self.x, self.y, self.z)

class ReadInfo:
    def __init__(self):
        self.baddr = ""
        self.rssi = ""
        self.time_to_go = 0
        self.command_id = 255
        self.compass = None

    def set_data(self, json_data):
    	self.baddr = json_data['baddr']
        self.rssi = json_data['rssi']
        self.time_to_go = json_data['time_to_go']
        self.command_id = json_data['command_id']
        self.compass = Compass(json_data['x'], json_data['y'], json_data['y']) 


def testi():
    test_data='{"baddr" : "71:E9:F6:72:21:FB", "rssi" : "-72", "time_to_go" : "0", "command_id" : "255", "x" : "-90", "y" : "147", "z" : "-127"}'
    	
    jsonD = json.loads(test_data)

    ri = ReadInfo()
    ri.set_data(jsonD)

    print "baddr={}, rssi={}, time_to_go={}, command_id={}, compass={}".format(ri.baddr, ri.rssi, ri.time_to_go, ri.command_id, ri.compass.to_string())

# main
testi()
