sudo docker network create mqtt
sudo docker network ls
sudo docker run -d --rm --name mqtt -p 1883:1883 --network mqtt mosquitto
# in the client.py script change ip address to ec2 instance public ip
sudo docker build -t streamingclient -f Dockerfile.client .
sudo docker run -it --rm --network mqtt --device=/dev/video0 streamingclient bash
python3 client.py
