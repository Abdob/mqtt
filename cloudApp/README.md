sudo docker network create mqtt
sudo docker network ls
sudo docker run -d --rm --name mqtt -p 1883:1883 --network mqtt mosquitto
sudo docker build -t streamingserver -f Dockerfile.server .
sudo docker run -it --rm --network mqtt streamingserver bash
python3 server.py
