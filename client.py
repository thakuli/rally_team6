import json
import threading
from time import sleep

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
    pass

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed OK")


def send_command(m1, m2, m_up, time, command_id):
    message = '{"m1": %i, "m2": %i, "m_up": %i, "time": %i, "command_id": %i}' % (m1, m2, m_up, time, command_id)
    client.publish('team7_write', message, qos=0, retain=False)
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

    thread = threading.Thread(target = client.loop_forever)
    thread.deamon = True
    thread.start()




    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.


    while True:
        #wsleep(1)
        input_var = raw_input('command: ')
        print input_var

        if input_var == "w":
            send_command(2, 1, 0, 150, 0)

        elif input_var == "s":
            send_command(1, 2, 0, 150, 0)

        elif input_var == "a":
            send_command(2, 2, 1, 150, 0)

        elif input_var == "d":
            send_command(1, 1, 1, 150, 0)

        elif input_var == "q":
            send_command(0, 0, 1, 150, 0)









