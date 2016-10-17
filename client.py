import json

import paho.mqtt.client as mqtt



# The callback for when the client receives a CONNACK response from the server.
import sys


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed OK")


def send_command(m1, m2, m_up, time, command_id):
    message = "{'m1': '%s', 'm2': '%s', 'm_up': '%s', 'time': '%s', 'command_id': '%s'}" % m1, m2, m_up, time, command_id
    #client.publish('team7_write', message, qos=0, retain=False)
    print message


if __name__ == "__main__":

    client = mqtt.Client(protocol=mqtt.MQTTv31)
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_subscribe = on_subscribe

    client.tls_insecure_set(True)

    client.connect("54.93.150.126", 1883, 60)


    client.subscribe("team7_read", 0)
    client.subscribe("team7_write", 0)




    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()

    while True:
        input_var = raw_input()

    if input_var == "w":
        send_command("1", "1", "0", "100", "0")

    elif input_var == "s":
        send_command("2", "2", "0", "100", "0")

    elif input_var == "a":
        send_command("1", "0", "1", "100", "0")

    elif input_var == "d":
        send_command("0", "1", "1", "100", "0")

    elif input_var == "q":
        send_command("0", "0", "1", "100", "0")









