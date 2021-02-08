import base64
import numpy as np
import paho.mqtt.client as mqtt
import cv2 as cv
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
    arr = np.frombuffer(msg.payload,dtype='uint8')
    print(arr.shape)
    img = cv.imdecode(arr,1)
    print(img.shape)
    save_string = '/apps/data/face_' + str(datetime.now()) + '.png'
    print("Storing png face ..")
    cv.imwrite(save_string, img)
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
