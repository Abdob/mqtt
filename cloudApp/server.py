import base64
import numpy as np
import paho.mqtt.client as mqtt
import os
from datetime import datetime

MQTT_BROKER = 'mqtt'
MQTT_RECEIVE = "streaming"

frame = np.zeros((240, 320, 3), np.uint8)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_RECEIVE)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global frame
    # Decoding the message
    save_string = 'face_' + str(datetime.now()) + '.bin'
    print("Storing face ..")
    f = open(save_string, 'w+b')
    f.write(msg.payload)
    f.close()
    # converting into numpy array from buffer


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER)

# Starting thread which will receive the frames
client.loop_start()

while 1:
    i=0
# Stop the Thread
client.loop_stop()
