# MQTT Broker
The Dockerfile in this directory starts a basic/default MQTT broker.  

The Dockerfile is simple:

```
FROM alpine
  
RUN apk update
RUN apk add mosquitto

CMD /usr/sbin/mosquitto                      
```

This image uses Alpine as a base then adds the mosquitto.  Finally, it starts the broker with the CMD value.

To build it, run the command:
```
sudo docker build -t mosquitto -f Dockerfile.mosquitto .
```

And to run on the default network:
```
sudo docker run -d -it --rm --name mosquitto -p 1883:1883 mosquitto
```
This starts an instance of the container named mosquitto, exposes port 1883, and will remove it when it is stopped.
