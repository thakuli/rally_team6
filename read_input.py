import paho.mqtt.client as mqtt
from ReadInfo import ReadInfo


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # print(msg.topic+" oho "+str(msg.payload))
    if (msg.topic == "team7_read"):
        ri = ReadInfo(read_json(msg.payload))
        ri.to_string()


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
