import paho.mqtt.client as mqtt
from Queue import PriorityQueue
from ReadInfo import *

MAX_DATA = 8
allowed_baddrs = ["6D:1E:FE:94:E6:44", "54:DE:10:BF:7A:80", "7D:B5:04:19:9E:68" ]
beacons = {}

for bc in allowed_baddrs:
    beacons[bc] = PriorityQueue(MAX_DATA)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

collect_time=2000
collect_start=0
def on_message_drafti(client, userdata, msg):
    baddr_data = []
    if (collect_start == 0):
        collect_start = current_time
    while ((current_time - collect_start) < collect_time):
        if (msg.topic == "team7_read"):
            jsonD = read_json(msg.payload)
            if (jsonD['baddr'] in allowed_baddrs):
                baddr_data.append(ReadInfo(read_json(msg.payload)))
    handler.handle_baddrdata(baddr_data)
    collect_start = 0
                


# The callback for when a PUBLISH message is received from the server.
msg_counter = 0
beacon_queue = PriorityQueue(MAX_DATA)
def on_message(client, userdata, msg):
    # print(msg.topic+" oho "+str(msg.payload))
    if (msg.topic == "team7_read"):
        jsonD = read_json(msg.payload)
        if (jsonD['baddr'] in allowed_baddrs):
            ri = ReadInfo(read_json(msg.payload))
            print "x={}, y={}, z={}".format(ri.compass.x, ri.compass.y, ri.compass.z)
            print "angle={}".format(ri.compass.get_angle2())

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed OK")


client = mqtt.Client(protocol=mqtt.MQTTv31)
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe

client.tls_insecure_set(True)

client.connect("54.93.150.126", 1883, 60)

client.subscribe("team7_read", 0)
# client.subscribe("team7_write", 0)




# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
