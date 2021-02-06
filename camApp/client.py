  
# Importing Libraries
import cv2 as cv
import numpy as np
import paho.mqtt.client as mqtt
import base64
import time
import os

# get the brokers address/name
MQTT_BROKER = 'mqtt'
# Topic
MQTT_SEND = "streaming"
# OpenCV time.  This is on device0
cap = cv.VideoCapture(0)
# Phao-MQTT Clinet
client = mqtt.Client()
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
# Connect
client.connect(MQTT_BROKER)
try:
 while True:
  start = time.time()
  # Read 
  _, frame = cap.read()
  frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(frame, 1.3, 5)
  # Encoding to jpeg
  for (x,y,w,h) in faces:
    crop_face = frame[y:y+h, x:x+w]
    _, buffer = cv.imencode('.png', crop_face)
    # this sends as text...
    msg = buffer.tobytes()
    # Publish
    client.publish(MQTT_SEND, msg)
    end = time.time()
    t = end - start
    fps = 1/t
    print('fps:', fps)
except:
 cap.release()
 client.disconnect()
 print("\nAll Done...")
