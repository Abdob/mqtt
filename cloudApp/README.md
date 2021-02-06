# Simple "Streaming"
In this example, we'll use MQTT to "stream" images.  Our client application will capture an image, publish it to a MQTT broker and our "server" application will listen for the images and display them on our screen.

First thing to do is to start your broker; see the mosquitto again.  You'll need two terminals again, each with the MQTT env var set correctly.
In terminal one, start the server: 
```
python3 server.py
```
And in the second terminal start the client:
```
python3 client.py
```

And you should see the images from you camera being displayed!
